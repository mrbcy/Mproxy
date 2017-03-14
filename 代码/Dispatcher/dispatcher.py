#-*- coding: utf-8 -*-
import time
import traceback

from conf.configloader import ConfigLoader
from proxyrechecker import ProxyRechecker
from zkutil.nodedetector import NodeDetector
from zkutil.noderegister import NodeRegister


class Dispatcher:

    def __init__(self):
        self.conf_loader = ConfigLoader()
        self.validator_controller = None


    def validator_node_change_listener(self,zk,node_path,children):
        try:
            # get all validators_name
            online_validator_names = []
            for child in children:
                validator_node = zk.get(path = node_path + str(child))
                if validator_node is not None:
                    online_validator_names.append(validator_node[0])
            print online_validator_names

            # judge whether all the validators on line
            validator_names = self.conf_loader.get_validator_list()

            is_all_online = True
            for name in validator_names:
                is_online = False
                for online_name in online_validator_names:
                    if name == online_name:
                        is_online = True
                if is_online == False:
                    is_all_online = False
                    break

            if is_all_online == True:
                self.validator_controller = NodeRegister(zkconn_str=self.conf_loader.get_zk_conn_str(),
                                                         node_path=self.conf_loader.control_node_path())
                self.validator_controller.regist('dispatcher',b'working')
            else:
                if self.validator_controller is not None:
                    self.validator_controller.close()

        except Exception as e:
            traceback.print_exc()


    def start_work(self):
        self.proxy_rechecker = ProxyRechecker()
        self.proxy_rechecker.start()
        self.validator_detector = NodeDetector(zkconn_str=self.conf_loader.get_zk_conn_str(),node_path=self.conf_loader.validator_node_path()
                                          ,node_change_listener = self.validator_node_change_listener)

        while True:
            time.sleep(1)


if __name__ == '__main__':
    dispatcher = Dispatcher()
    dispatcher.start_work()