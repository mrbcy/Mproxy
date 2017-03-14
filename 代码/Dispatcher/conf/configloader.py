#-*- coding: utf-8 -*-
import ConfigParser
import os


class ConfigLoader:
    def __init__(self):
        # get the project path
        thePath = os.getcwdu()
        if thePath.find("Dispatcher\\") > 0:
            thePath = thePath[:thePath.find("Dispatcher\\") + len("Dispatcher\\")]
        else:
            thePath += "\\"
        print thePath
        self.cp = ConfigParser.SafeConfigParser()
        self.cp.read(thePath + 'dispatcher.cfg')

    def get_zk_conn_str(self):
        return self.cp.get('zookeeper','zk_conn_str')

    def control_node_path(self):
        return self.cp.get('zookeeper','control_node_path')

    def validator_node_path(self):
        return self.cp.get('zookeeper','validator_node_path')

    def get_log_file_name(self):
        return self.cp.get('log','log_file_name')

    def get_validator_list(self):
        text =  self.cp.get('validator','validator_list')
        return text.split(',')

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

    def get_kafka_bootstrap_servers(self):
        text = self.cp.get('kafka','bootstrap_servers')
        return text.split(',')