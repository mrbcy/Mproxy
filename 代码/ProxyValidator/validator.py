#-*- coding: utf-8 -*-
import logging
import re
import threading

import requests
import time


class ProxyValidator(threading.Thread):
    def __init__(self, queue, submit_util):
        threading.Thread.__init__(self)
        self.queue = queue
        self.submit_util = submit_util
        self.is_working = False
        self.is_finish = False

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
        self.valid_proxy()

    def valid_proxy(self):
        headers = {
            "Host": "www.sogou.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Cookie": "CXID=AFB58656EB6137C12D0E4FF12BC6DFFE; SUV=1484628390086037; m=FAB6EC92D3062F7D84CC06636E62F609; ABTEST=0|1486986265|v17; ad=oe45yZllll2Y$gmTlllllVAIWEtlllllJa0oJyllll9lllll9Zlll5@@@@@@@@@@; SUID=B96B30B65412940A00000000586E6482; ld=okllllllll2Y7@v2lllllVA8dw1lllllH0xrAlllll9lllllpZlll5@@@@@@@@@@; YYID=FAB6EC92D3062F7D84CC06636E62F609; SNUID=441BB6B17B7E35AEB86CFBF37CECC35E; usid=Ibgtjb1FmwpmVEd9; IPLOC=CN1101; browerV=8; osV=1",
            "Connection": "keep-alive",
            "Upgrade - Insecure - Requests": "1"
        }
        try:
            start_time = time.clock()
            res = requests.get('http://www.sogou.com/', proxies={'http': self.proxy_item['ip']+':'+self.proxy_item['port']}, timeout = 10)
            end_time = time.clock()
            time_consume = end_time - start_time
            regex = """050897"""
            pattern = re.compile(regex)
            if re.search(pattern=pattern, string=res.text) is not None and time_consume <= 5:
                logging.info("proxy %s:%s is available, costs %f s" % (self.proxy_item['ip'],self.proxy_item['port'],time_consume))
                self.submit_util.send_msg(self.proxy_item)
            else:
                logging.info("proxy %s:%s is unavailable, costs %f s" % (self.proxy_item['ip'], self.proxy_item['port'],time_consume))

        except Exception as e:
            logging.info("proxy %s:%s is unavailable, exception catch %s" % (self.proxy_item['ip'], self.proxy_item['port'],e.message))

        finally:
            self.is_finish = True


# def valid_proxy():
#     headers = {
#         "Host": "www.sogou.com",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#         "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Accept-Encoding": "gzip, deflate",
#         "Cookie": "CXID=AFB58656EB6137C12D0E4FF12BC6DFFE; SUV=1484628390086037; m=FAB6EC92D3062F7D84CC06636E62F609; ABTEST=0|1486986265|v17; ad=oe45yZllll2Y$gmTlllllVAIWEtlllllJa0oJyllll9lllll9Zlll5@@@@@@@@@@; SUID=B96B30B65412940A00000000586E6482; ld=okllllllll2Y7@v2lllllVA8dw1lllllH0xrAlllll9lllllpZlll5@@@@@@@@@@; YYID=FAB6EC92D3062F7D84CC06636E62F609; SNUID=441BB6B17B7E35AEB86CFBF37CECC35E; usid=Ibgtjb1FmwpmVEd9; IPLOC=CN1101; browerV=8; osV=1",
#         "Connection": "keep-alive",
#         "Upgrade - Insecure - Requests": "1"
#     }
#     try:
#         start_time = time.clock()
#         res = requests.get('http://www.sogou.com/', proxies={'http': '61.144.194.67:9000'})
#         end_time = time.clock()
#         time_consume = end_time - start_time
#         regex = """050897"""
#         pattern = re.compile(regex)
#         print res.text
#         if re.search(pattern=pattern, string=res.text) is not None and time_consume <= 3:
#             print "proxy is available"
#         else:
#             print "proxy is unavailable"
#     except Exception as e:
#         print "Exception catched: " + str(e)
#
# if __name__ == '__main__':
#     valid_proxy()