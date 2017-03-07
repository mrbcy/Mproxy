#-*- coding: utf-8 -*-
import threading

class ProxyQueue:

    def __init__(self):
        self.lock = threading.Lock()
        self.proxy_list = []

    def add_proxy(self,proxy_item):
        self.lock.acquire()
        self.proxy_list.append(proxy_item)
        self.lock.release()

    def get_proxy(self):
        proxy_item = None
        self.lock.acquire()
        proxy_count = len(self.proxy_list)
        if proxy_count > 0:
            proxy_item = self.proxy_list[0]
        self.lock.release()
        return proxy_item

    def pop_proxy(self):
        proxy_item = None
        self.lock.acquire()
        proxy_count = len(self.proxy_list)
        if proxy_count > 0:
            proxy_item = self.proxy_list.pop()
        self.lock.release()
        return proxy_item

    def get_proxy_count(self):
        proxy_count = 0
        self.lock.acquire()
        proxy_count = len(self.proxy_list)
        self.lock.release()
        return proxy_count