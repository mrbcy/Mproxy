# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging

from kafka import KafkaProducer

from xicidaili.conf.configloader import ConfigLoader
from xicidaili.proxyrecord.recorder import XicidailiProxyRecorder


class XicidailiPipeline(object):
    def process_item(self, item, spider):
        return item

class XicidailiKafkaPipeline(object):
    def __init__(self):
        self.conf_loader = ConfigLoader()
        self.producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                     bootstrap_servers=self.conf_loader.get_kafka_bootstrap_servers())
        self.proxy_recorder = XicidailiProxyRecorder(mongodb_host=self.conf_loader.get_mongodb_host())

    def __del__(self):
        if self.producer is not None:
            self.producer.close()

    def process_item(self, item, spider):
        try:
            log_msg = "Get a proxy[%(ip)s\t%(port)s\t%(anonymity)s\t%(type)s\t%(location)s]. Task Id is:%(task_id)s" % item
            logging.info(log_msg)
            if self.proxy_recorder.find_repeat_proxy(item['ip']) is None:
                logging.debug(item['ip'] + ' is not repeat')
                self.producer.send('unchecked-servers', item.__dict__)  # Makes the item could be JSON serializable
                self.proxy_recorder.save_proxy(item)
            else:
                logging.debug(item['ip'] + ' is repeat, not submit to Kafka cluster')

        except Exception as e:
            logging.exception("An Error Happens")

        return item