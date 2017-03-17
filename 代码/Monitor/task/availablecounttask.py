#-*- coding: utf-8 -*-
import os
import threading

import time
import traceback

from conf.configloader import ConfigLoader
from service.proxyservice import ProxyService
from sms.smsutil import SmsUtil


class AvailableCountTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.proxy_service = ProxyService()
        self.conf_loader = ConfigLoader()

    def run(self):

        while True:
            count = self.proxy_service.get_avaliable_proxy_count()
            if count < 4500:
                try:
                    # start spiders
                    exit_code = os.system(self.conf_loader.get_start_kuaidaili_command())
                    print exit_code
                    if exit_code != 0:
                        SmsUtil.send_sms('Mproxy', '快代理爬虫运行出错', '无')

                    time.sleep(5)

                    exit_code = os.system(self.conf_loader.get_start_xicidaili_command())
                    print exit_code
                    if exit_code != 0:
                        SmsUtil.send_sms('Mproxy', '西刺代理爬虫运行出错', '无')
                except Exception as e:
                    traceback.print_exc()
                    SmsUtil.send_sms('Mproxy','启动爬虫出错','无')

            elif count < 2000:
                SmsUtil.send_sms('Mproxy', '代理服务器数量不足', str(count))

            time.sleep(60*60*2)