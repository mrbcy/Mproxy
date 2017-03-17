#-*- coding: utf-8 -*-
from dao.proxydao import ProxyDao


class ProxyService():
    def __init__(self):
        self.proxy_dao = ProxyDao()

    def find_proxy_last_validate_time(self):
        return self.proxy_dao.find_proxy_last_validate_time()

    def get_avaliable_proxy_count(self):
        return self.proxy_dao.get_avaliable_proxy_count()