#-*- coding: utf-8 -*-
import ConfigParser
import os


class ConfigLoader:
    def __init__(self):
        # get the project path
        dir_name = "Monitor" + os.sep
        thePath = os.getcwdu()
        if thePath.find(dir_name) > 0:
            thePath = thePath[:thePath.find(dir_name) + len(dir_name)]
        else:
            thePath += os.sep
        print thePath
        self.cp = ConfigParser.SafeConfigParser()
        self.cp.read(thePath + 'monitor.cfg')

    def get_app_key(self):
        return self.cp.get('sms','appkey')

    def get_secret_key(self):
        return self.cp.get('sms','secret')

    def get_sign_name(self):
        return self.cp.get('sms','sign_name')

    def get_sms_template_code(self):
        return self.cp.get('sms','sms_template_code')

    def get_phone_num(self):
        return self.cp.get('sms','phone_num')

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

    def get_start_kuaidaili_command(self):
        return self.cp.get('os','start_kuaidaili_command')

    def get_start_xicidaili_command(self):
        return self.cp.get('os','start_xicidaili_command')