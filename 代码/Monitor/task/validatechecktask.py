#-*- coding: utf-8 -*-
import os
import threading

import time
import traceback

import datetime

from service.proxyservice import ProxyService
from sms.smsutil import SmsUtil


class ValidateCheckTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.proxy_service = ProxyService()

    def run(self):

        while True:
            last_validate_time = self.proxy_service.find_proxy_last_validate_time()
            now = datetime.datetime.now()
            seconds = (now - last_validate_time).total_seconds()

            if seconds > 12 * 60 * 60:
                SmsUtil.send_sms('Mproxy', '超过12小时未执行验证', '无')

            time.sleep(60*60*6)