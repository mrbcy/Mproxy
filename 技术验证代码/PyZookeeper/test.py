#-*- coding: utf-8 -*-
import time
from kazoo.client import KazooClient
from kazoo.protocol.states import KazooState

zk = KazooClient(hosts='amaster:2181,anode1:2181,anode2:2181')

def my_listener(state):
    if state == KazooState.LOST:
        # Register somewhere that the session was lost
        print "Now Lost"
    elif state == KazooState.SUSPENDED:
        # Handle being disconnected from Zookeeper
        print "Now Suspended"
    else:
        # Handle being connected/reconnected to Zookeeper
        print "Now Connected"

def func():
    zk.add_listener(my_listener)
    zk.start()
    children = zk.get_children('/app1')
    print children
    create_result = zk.create('/mproxy/test/validator/validator',b'validator_huabei_1',ephemeral=True,sequence=True,makepath=True)
    print create_result
    time.sleep(200)
    zk.stop()


@zk.ChildrenWatch('/mproxy/test/validator')
def watch_children(children):
    print("Children are now: %s" % children)

if __name__ == '__main__':
    func()