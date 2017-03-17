#-*- coding: utf-8 -*-
import datetime

from dao.proxydao import ProxyDao
from dao.proxystatus import ProxyStatus
from domain.proxydaoitem import ProxyDaoItem

proxy_dao = ProxyDao()

def test_get_proxy_count():
    global proxy_dao
    print proxy_dao.get_avaliable_proxy_count()

def test_get_last_validate_time():
    global proxy_dao
    last_validate_time = proxy_dao.find_proxy_last_validate_time()
    print type(last_validate_time)
    print last_validate_time

if __name__ == '__main__':
    test_get_last_validate_time()