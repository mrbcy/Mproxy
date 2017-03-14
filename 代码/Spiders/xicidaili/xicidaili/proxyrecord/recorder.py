#-*- coding: utf-8 -*-
import logging

import datetime
from pymongo import MongoClient


class XicidailiProxyRecorder:

    def __init__(self,mongodb_host='localhost',port=27017,record_days=3):
        self.client = MongoClient(mongodb_host, port)
        self.db = self.client.mproxy
        self.collection = self.db.xicidaili_proxy_records
        self.record_days = record_days

    def save_proxy(self,proxy_item):
        try:
            record = {}
            record['ip'] = proxy_item['ip']
            record['update_time'] = datetime.datetime.now()
            self.collection.save(record)
        except Exception as e:
            logging.exception("An Error Happens")

    def find_repeat_proxy(self,ip):
        try:
            d = datetime.datetime.now()
            d = d - datetime.timedelta(days=self.record_days)

            return self.collection.find_one({'ip':ip,'update_time':{"$gt": d}})
        except Exception as e:
            logging.exception("An Error Happens")