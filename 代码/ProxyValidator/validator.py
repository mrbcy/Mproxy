#-*- coding: utf-8 -*-
import logging
import re
import threading

import requests
import time

from conf.configloader import ConfigLoader


class ProxyValidator(threading.Thread):
    def __init__(self, queue, submit_util):
        threading.Thread.__init__(self)
        self.queue = queue
        self.submit_util = submit_util
        self.is_working = False
        self.is_finish = False
        self.config_loader = ConfigLoader()

    def is_finish(self):
        return self.is_finish

    def is_start(self):
        return self.is_working

    def run(self):
        if self.is_working == True:
            logging.debug("The task has already started")
            return

        self.is_working = True
        proxy_item = self.queue.pop_proxy()
        if proxy_item is None:
            self.is_finish = True
            return
        self.proxy_item = proxy_item
        self.proxy_item['validator_name'] = self.config_loader.get_validator_name()
        self.valid_proxy()

    def valid_proxy(self):
        headers = {
            "Host": "cn.bing.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Cookie": "MUID=0367654CF2046E403DCA6F4DF6046DFC; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=5C54DB461CC44305BE5560497C7E1932; SRCHUSR=DOB=20170310; _EDGE_S=SID=2CDBF24456B266310767F80557136780; MUIDB=0367654CF2046E403DCA6F4DF6046DFC; WLS=TS=63624706084; _SS=SID=2CDBF24456B266310767F80557136780&bIm=149196&HV=1489109297; SRCHHPGUSR=CW=864&CH=679&DPR=1.25&UTC=480",
            "Connection": "keep-alive",
            "Upgrade - Insecure - Requests": "1"
        }
        try:
            start_time = time.clock()
            res = requests.get('http://cn.bing.com/', proxies={'http': self.proxy_item['ip']+':'+self.proxy_item['port']}, timeout = 20)
            end_time = time.clock()
            time_consume = end_time - start_time
            regex = """10036305"""
            pattern = re.compile(regex)
            if re.search(pattern=pattern, string=res.text) is not None and time_consume <= 20:
                self.proxy_item['validate_result'] = True
                logging.info("proxy %s:%s is available, costs %f s" % (self.proxy_item['ip'],self.proxy_item['port'],time_consume))

            else:
                self.proxy_item['validate_result'] = False
                logging.info("proxy %s:%s is unavailable, costs %f s" % (self.proxy_item['ip'], self.proxy_item['port'],time_consume))

        except Exception as e:
            self.proxy_item['validate_result'] = False
            logging.info("proxy %s:%s is unavailable, exception catch %s" % (self.proxy_item['ip'], self.proxy_item['port'],e.message))

        finally:
            self.submit_util.send_msg(self.proxy_item)
            self.is_finish = True
