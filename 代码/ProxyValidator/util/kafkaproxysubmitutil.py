#-*- coding: utf-8 -*-
import json
import threading

from kafka import KafkaProducer


class KafkaProxySubmitUtil:
    def __init__(self, bootstrap_server,topic='checked-servers'):
        self.producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                     bootstrap_servers=bootstrap_server)
        self.lock = threading.Lock()
        self.topic = topic

    def __del__(self):
        if self.producer is not None:
            self.producer.close()

    def send_msg(self,msg):
        self.lock.acquire()
        self.producer.send(self.topic, msg)
        self.lock.release()