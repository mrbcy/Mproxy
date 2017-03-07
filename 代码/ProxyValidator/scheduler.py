#-*- coding: utf-8 -*-
import logging
import time
from logging.handlers import RotatingFileHandler

from kafkaproxylistener import KafkaProxyListener
from util.kafkaproxysubmitutil import KafkaProxySubmitUtil
from util.proxyqueue import ProxyQueue
from validator import ProxyValidator


def init_log():
    logging.getLogger().setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

    # add log ratate
    Rthandler = RotatingFileHandler('proxy_validator.log', maxBytes=10 * 1024 * 1024, backupCount=100,
                                    encoding="gbk")
    Rthandler.setLevel(logging.INFO)
    Rthandler.setFormatter(formatter)
    logging.getLogger().addHandler(Rthandler)

if __name__ == '__main__':
    init_log()
    logger = logging.getLogger()
    validator_num = 10
    validators = []
    logging.debug('ahahah')

    queue = ProxyQueue()
    # queue.add_proxy({'ip':'182.254.129.123','port':'80'})
    # queue.add_proxy({'ip':'101.53.101.172','port':'9999'})
    # queue.add_proxy({'ip':'106.46.136.204','port':'808'})
    # queue.add_proxy({'ip':'117.90.1.34','port':'9000'})
    # queue.add_proxy({'ip':'117.90.6.134','port':'9000'})
    # queue.add_proxy({'ip':'125.123.76.134','port':'8998'})
    # queue.add_proxy({'ip':'125.67.75.53','port':'9000'})
    # queue.add_proxy({'ip':'115.28.169.160','port':'8118'})
    # queue.add_proxy({'ip':'117.90.1.35','port':'9000'})
    # queue.add_proxy({'ip':'111.72.126.161','port':'808'})
    # queue.add_proxy({'ip':'121.232.148.94','port':'9000'})
    # queue.add_proxy({'ip':'117.90.7.106','port':'9000'})

    proxy_listener = KafkaProxyListener(queue=queue)
    proxy_listener.start()

    available_proxies = ProxyQueue()
    submit_util = KafkaProxySubmitUtil(bootstrap_server=['amaster:9092','anode1:9092','anode2:9092'])

    for i in xrange(validator_num):
        validators.append(ProxyValidator(queue=queue, submit_util=submit_util))
        validators[i].start()

    while True:
        is_finish = True
        for i in xrange(validator_num):
            if validators[i].is_finish == False:
                is_finish = False
                break

        # if queue.get_proxy_count() == 0 and is_finish == True:
            # break
        for i in xrange(validator_num):
            if validators[i].is_finish == True and queue.get_proxy_count() > 0:
                validators[i] = ProxyValidator(queue=queue,submit_util = submit_util)
                validators[i].start()
                logging.debug("分配一个新的验证器开始工作")

        logging.debug("当前任务列表长度：" + str(queue.get_proxy_count()))
        time.sleep(1)
    proxy_listener.raiseExc(Exception)
    print "代理服务器验证完毕。"