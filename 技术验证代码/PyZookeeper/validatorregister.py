#-*- coding: utf-8 -*-
import threading
import time
from kazoo.client import KazooClient
from kazoo.protocol.states import KazooState

class InfoKeeper(threading.Thread):
    def __init__(self,register):
        threading.Thread.__init__(self)
        self.register=register

    def run(self):
        time.sleep(0.25)
        if self.register.zk_node is None:
            print "create method has not been called"
            return
        check_result = self.register.zk.exists(self.register.validator_path)
        if check_result is None:
            # redo the regist
            print "redo the regist"
            self.register.regist()
        else:
            print "the path remain exists"

class ValidatorRegister:
    def __init__(self):
        self.zk = KazooClient(hosts='amaster:2181,anode1:2181,anode2:2181')
        self.zk_node = None
        self.validator_path = '/mproxy/validators/'
        self.zk.add_listener(self.conn_state_watcher)
        self.zk.start()


    def __del__(self):
        self.zk.close()

    def regist(self):
        self.zk_node = self.zk.create(self.validator_path + 'validator',bytes('validator_huabei_1'),ephemeral=True,sequence=True,makepath=True)

    def close(self):
        self.zk.close()

    def conn_state_watcher(self, state):
        if state == KazooState.CONNECTED:
            print "Now connected"

            if self.zk_node is None:
                print "create method has not been called"
                return
            info_keeper = InfoKeeper(self)
            info_keeper.start()
        elif state == KazooState.LOST:
            print "Now lost"
        else:
            print "Now suspended"


if __name__ == '__main__':
    register = ValidatorRegister()
    register.regist()
