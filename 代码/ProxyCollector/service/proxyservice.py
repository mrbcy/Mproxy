#-*- coding: utf-8 -*-
import datetime

from dao.proxydao import ProxyDao
from dao.proxystatus import ProxyStatus
from domain.proxydaoitem import ProxyDaoItem


class ProxyService:

    def __init__(self):
        self.proxy_dao = ProxyDao()

    def find_proxy_by_addr(self,proxy_addr):
        return self.proxy_dao.find_proxy_by_addr(proxy_addr)

    def find_proxy_need_to_recheck(self):
        now = datetime.datetime.now();
        timestamp = now - datetime.timedelta(hours=6)
        return self.proxy_dao.find_proxy_need_to_recheck(timestamp)

    def save_proxy(self,validation_result_item):
        # Firstly, we look up the proxy_info in db
        dao_item = self.proxy_dao.find_proxy_by_addr(validation_result_item.ip + ':'+validation_result_item.port)
        insert_flag = False
        if dao_item is None:
            dao_item = ProxyDaoItem()
            dao_item.proxy_addr = validation_result_item.ip + ':'+validation_result_item.port
            dao_item.anonymity = validation_result_item.anonymity
            dao_item.location = validation_result_item.location
            dao_item.type = validation_result_item.type
            dao_item.create_time = datetime.datetime.now()
            insert_flag = True

        if validation_result_item.validate_result == True:
            dao_item.last_validate_time = datetime.datetime.now()
            dao_item.last_available_time = datetime.datetime.now()
            dao_item.retry_count = 0
            dao_item.status = ProxyStatus.AVAILABLE
        else:
            dao_item.last_validate_time = datetime.datetime.now()
            dao_item.retry_count += 1
            if dao_item.retry_count >= 3:
                dao_item.status = ProxyStatus.PERMANENT_UNAVAILABLE
            else:
                dao_item.status = ProxyStatus.TEMP_UNAVAILABLE

        if insert_flag == True:
            self.proxy_dao.insert_proxy(dao_item)
        else:
            self.proxy_dao.update_proxy(dao_item)