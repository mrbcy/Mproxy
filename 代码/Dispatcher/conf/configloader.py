#-*- coding: utf-8 -*-
import ConfigParser


class ConfigLoader:
    def __init__(self):
        self.cp = ConfigParser.SafeConfigParser()
        self.cp.read('dispatcher.cfg')

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
