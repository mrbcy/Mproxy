#-*- coding: utf-8 -*-
import time
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch




class ValidatorDetector:

    def __init__(self):
        self.validator_path = '/mproxy/validators/'
        self.zk = KazooClient(hosts='amaster:2181,anode1:2181,anode2:2181')
        self.validator_children_watcher = ChildrenWatch(client=self.zk,path=self.validator_path,func=self.validator_watcher_fun)
        self.zk.start()

    def validator_watcher_fun(self,children):
        for child in children:
            validator_name = self.zk.get(path=self.validator_path + str(child))
            print validator_name[0]
        print "The children now are:", children


    def __del__(self):
        self.zk.close()





if __name__ == '__main__':
    detector = ValidatorDetector()
    time.sleep(300)