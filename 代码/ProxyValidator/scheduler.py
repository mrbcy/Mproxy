#-*- coding: utf-8 -*-
import logging
import time
from logging.handlers import RotatingFileHandler

from conf.configloader import ConfigLoader
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

    queue = ProxyQueue()

    config_loader = ConfigLoader()

    proxy_listener = KafkaProxyListener(queue=queue)
    proxy_listener.start()

    available_proxies = ProxyQueue()
    submit_util = KafkaProxySubmitUtil(bootstrap_server=config_loader.get_kafka_bootstrap_servers())

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