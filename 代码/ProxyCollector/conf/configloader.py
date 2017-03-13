#-*- coding: utf-8 -*-
import ConfigParser
import os


class ConfigLoader:
    def __init__(self):
        # get the project path
        thePath = os.getcwdu()
        if thePath.find("ProxyCollector\\") > 0:
            thePath = thePath[:thePath.find("ProxyCollector\\") + len("ProxyCollector\\")]
        else:
            thePath += "\\"
        print thePath
        self.cp = ConfigParser.SafeConfigParser()
        self.cp.read(thePath + 'collector.cfg')

    def get_validator_list(self):
        text =  self.cp.get('validator','validator_list')
        return text.split(',')

    def get_mysql_host(self):
        return self.cp.get('mysql','host')

    def get_mysql_port(self):
        return int(self.cp.get('mysql','port'))

    def get_mysql_user(self):
        return self.cp.get('mysql','user')

    def get_mysql_pwd(self):
        return self.cp.get('mysql','password')

    def get_mysql_db_name(self):
        return self.cp.get('mysql','db_name')
