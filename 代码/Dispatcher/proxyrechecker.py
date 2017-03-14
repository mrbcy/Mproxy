#-*- coding: utf-8 -*-
import json
import threading
import uuid

import time
from kafka import KafkaProducer

from conf.configloader import ConfigLoader
from service.proxyservice import ProxyService


class ProxyRechecker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.conf_loader = ConfigLoader()
        self.producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                      bootstrap_servers=self.conf_loader.get_kafka_bootstrap_servers())
        self.proxy_service = ProxyService()

    def run(self):
        while True:
            dao_items = self.proxy_service.find_proxy_need_to_recheck()

            if dao_items is not None:
                print "Proxy Rechecker 提交 %s 个代理服务器进行重新验证" % (len(dao_items))
                for dao_item in dao_items:
                    # construct validate bean
                    validate_item = {'_values':{}}
                    validate_item['_values']['task_id'] = str(uuid.uuid4())
                    validate_item['_values']['ip'] = dao_item.proxy_addr.split(':')[0]
                    validate_item['_values']['port'] = dao_item.proxy_addr.split(':')[1]
                    validate_item['_values']['anonymity'] = dao_item.anonymity
                    validate_item['_values']['type'] = dao_item.type
                    validate_item['_values']['location'] = dao_item.location
                    validate_item['_values']['spider_name'] = "mproxy_dispatcher"
                    self.producer.send('unchecked-servers',validate_item)

            time.sleep(60*60*3)
