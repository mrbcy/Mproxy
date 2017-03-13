#-*- coding: utf-8 -*-
import datetime

from dao.proxydao import ProxyDao
from dao.proxystatus import ProxyStatus
from domain.proxydaoitem import ProxyDaoItem

proxy_dao = ProxyDao()

def test_insert_proxy():
    global proxy_dao
    dao_item = ProxyDaoItem()
    dao_item.proxy_addr = "127.0.0.1:5002"
    dao_item.location = "北京 海淀 移动"
    dao_item.status = ProxyStatus.PERMANENT_UNAVAILABLE
    dao_item.anonymity = "高匿名"
    dao_item.last_available_time = datetime.datetime.now()
    dao_item.last_validate_time = datetime.datetime.now()
    dao_item.retry_count = 0
    dao_item.type = "HTTP"

    proxy_dao.insert_proxy(dao_item)

def test_find_one():
    global proxy_dao
    dao_item = proxy_dao.find_proxy_by_addr('127.0.0.1:5002')
    print dao_item

def test_update():
    global proxy_dao
    dao_item = proxy_dao.find_proxy_by_addr('127.0.0.1:5002')
    dao_item.location = "测试位置"
    dao_item.type = "HTTP,HTTPS"
    dao_item.anonymity = '透明'
    dao_item.status = ProxyStatus.AVAILABLE
    dao_item.retry_count = 3
    dao_item.last_available_time = datetime.datetime.now()
    dao_item.last_validate_time = datetime.datetime.now()
    proxy_dao.update_proxy(dao_item)

def test_find_proxy_need_to_recheck():
    global  proxy_dao
    now = datetime.datetime.now();
    timestamp = now - datetime.timedelta(hours=6)
    proxy_items = proxy_dao.find_proxy_need_to_recheck(timestamp)
    print proxy_items

if __name__ == '__main__':
    test_find_proxy_need_to_recheck()