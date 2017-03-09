#-*- coding: utf-8 -*-
import ConfigParser


class ConfigLoader:
    def __init__(self):
        self.cp = ConfigParser.SafeConfigParser()
        self.cp.read('proxy_validator.cfg')

    def get_kafka_bootstrap_servers(self):
        text = self.cp.get('kafka','bootstrap_servers')
        return text.split(',')

    def get_log_file_name(self):
        return self.cp.get('log','log_file_name')

    def get_validator_name(self):
        return self.cp.get('validator','validator_name')

    def get_zk_conn_str(self):
        return self.cp.get('zookeeper','zk_conn_str')

    def get_control_node_path(self):
        return self.cp.get('zookeeper','control_node_path')

    def get_validator_node_path(self):
        return self.cp.get('zookeeper','validator_node_path')