#-*- coding: utf-8 -*-

class ProxyDaoItem:
    def __init__(self):
        self.proxy_addr = None
        self.location = None
        self.anonymity = None
        self.type = None
        self.last_validate_time = None
        self.retry_count = 0
        self.last_available_time = None
        self.status = None