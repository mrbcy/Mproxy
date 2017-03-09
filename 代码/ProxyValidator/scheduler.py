#-*- coding: utf-8 -*-
import logging
import time
from logging.handlers import RotatingFileHandler

from conf.configloader import ConfigLoader
from kafkaproxylistener import KafkaProxyListener
from util.kafkaproxysubmitutil import KafkaProxySubmitUtil
from util.proxyqueue import ProxyQueue
from validator import ProxyValidator
from zkutil.nodedetector import NodeDetector
from zkutil.noderegister import NodeRegister

class Scheduler:
    def __init__(self):
        self.init_log()

    def init_log(self):
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

    def control_signal_change_listener(self,zk,node_path,children):
        try:
            if len(children) > 0:  # now working
                logging.debug("接到控制器指令：开始工作")
                self.work_flag = True
                if self.proxy_listener is not None:
                    self.proxy_listener.raiseExc(Exception)
                self.proxy_listener = KafkaProxyListener(queue=self.queue)
                self.proxy_listener.start()
            else:
                logging.debug("接到控制器指令：停止工作")
                self.work_flag = False
                if self.proxy_listener is not None:
                    self.proxy_listener.raiseExc(Exception)
                    self.proxy_listener = None
        except Exception as e:
            logging.exception("Exception happens")



    def start_working(self):

        self.work_flag = False  # will not do the work unless receive the remote control signal
        validator_num = 10
        validators = []

        self.queue = ProxyQueue()

        config_loader = ConfigLoader()

        self.proxy_listener = None

        validator_register = NodeRegister(zkconn_str=config_loader.get_zk_conn_str(),
                                          node_path=config_loader.get_validator_node_path())
        validator_register.regist('validator', bytes(config_loader.get_validator_name()))

        control_receiver = NodeDetector(zkconn_str=config_loader.get_zk_conn_str(),
                                        node_path=config_loader.get_control_node_path()
                                        ,node_change_listener=self.control_signal_change_listener)

        submit_util = KafkaProxySubmitUtil(bootstrap_server=config_loader.get_kafka_bootstrap_servers())

        for i in xrange(validator_num):
            validators.append(ProxyValidator(queue=self.queue, submit_util=submit_util))
            validators[i].start()

        while True:

            for i in xrange(validator_num):
                if validators[i].is_finish == True and self.queue.get_proxy_count() > 0 and self.work_flag == True:
                    validators[i] = ProxyValidator(queue=self.queue, submit_util=submit_util)
                    validators[i].start()
                    logging.debug("分配一个新的验证器开始工作")

            if self.work_flag == True:
                logging.debug("当前任务列表长度：" + str(self.queue.get_proxy_count()))
            else:
                logging.debug("正在等待调度器的启动指令")
            time.sleep(1)

        print "代理服务器验证完毕。"

if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.start_working()