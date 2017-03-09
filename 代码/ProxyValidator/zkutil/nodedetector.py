#-*- coding: utf-8 -*-
import time
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch


class NodeDetector:

    def __init__(self,zkconn_str,node_path,node_change_listener = None):
        # self.node_path = '/mproxy/validators/'
        self.node_path = node_path
        # self.zk = KazooClient(hosts='amaster:2181,anode1:2181,anode2:2181')
        self.zk = KazooClient(hosts=zkconn_str)
        self.node_change_listener = node_change_listener
        self.children_watch = ChildrenWatch(client=self.zk, path=self.node_path, func=self.node_watcher_fun)
        self.zk.start()

    def node_watcher_fun(self, children):
        if self.node_change_listener is not None:
            self.node_change_listener(zk = self.zk,node_path=self.node_path,children=children)



    def __del__(self):
        self.zk.stop()
        self.zk.close()
