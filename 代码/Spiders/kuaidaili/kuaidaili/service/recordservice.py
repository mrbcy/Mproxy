#-*- coding: utf-8 -*-
import datetime

from kuaidaili.dao.recorddao import RecordDao
from kuaidaili.domain.recorditem import RecordItem


class RecordService:

    def __init__(self):
        self.record_dao = RecordDao()

    def find_record_by_addr(self,proxy_addr):
        return self.record_dao.find_record_by_addr(proxy_addr)

    def save_record(self,item):
        # Firstly, we look up the proxy_info in db
        record_item = self.record_dao.find_record_by_addr(item['ip'] + ':' + str(item['port']))
        if record_item is None:
            record_item = RecordItem()
            record_item.proxy_addr = item['ip'] + ':' + str(item['port'])
            record_item.create_time = datetime.datetime.now()
            self.record_dao.insert_record(record_item)
