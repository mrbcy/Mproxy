#-*- coding: utf-8 -*-
import ConfigParser


class ConfigLoader:
    def __init__(self):
        self.cp = ConfigParser.SafeConfigParser()
        self.cp.read('xicidaili_spider.cfg')

    def get_mongodb_host(self):
        return self.cp.get('mongodb','host')

    def get_kafka_bootstrap_servers(self):
        text = self.cp.get('kafka','bootstrap_servers')
        return text.split(',')

    def get_log_file_name(self):
        return self.cp.get('log','log_file_name')
