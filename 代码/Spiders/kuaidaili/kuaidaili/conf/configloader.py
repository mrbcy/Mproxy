#-*- coding: utf-8 -*-
import ConfigParser


class ConfigLoader:
    def __init__(self):
        self.cp = ConfigParser.SafeConfigParser()
        self.cp.read('kuaidaili_spider.cfg')

    def get_mongodb_host(self):
        return self.cp.get('mongodb','host')

    def get_kafka_bootstrap_servers(self):
        text = self.cp.get('kafka','bootstrap_servers')
        return text.split(',')

    def get_log_file_name(self):
        return self.cp.get('log','log_file_name')

    def get_mysql_host(self):
        return self.cp.get('mysql', 'host')


    def get_mysql_port(self):
        return int(self.cp.get('mysql', 'port'))


    def get_mysql_user(self):
        return self.cp.get('mysql', 'user')


    def get_mysql_pwd(self):
        return self.cp.get('mysql', 'password')


    def get_mysql_db_name(self):
        return self.cp.get('mysql', 'db_name')