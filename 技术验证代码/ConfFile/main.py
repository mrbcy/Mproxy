#-*- coding: utf-8 -*-
import ConfigParser


def func():
    cp = ConfigParser.SafeConfigParser()
    cp.read('kuaidaili_spider.cfg')

    print 'mongodb host',cp.get('mongodb','host')
    print 'kafka bootstrap_servers',cp.get('kafka','bootstrap_servers')
    print 'log file name',cp.get('log','log_file_name')
    print 'zookeeper conn string',cp.get('zookeeper','conn_str')

if __name__ == '__main__':
    func()