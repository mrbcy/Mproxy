#-*- coding: utf-8 -*-
import traceback

import top
from conf.configloader import ConfigLoader


class SmsUtil:
    conf_loader = ConfigLoader()
    @classmethod
    def send_sms(cls,system_name,exception_name,key_prompt):
        url = "gw.api.taobao.com"
        appkey = cls.conf_loader.get_app_key()
        secret = cls.conf_loader.get_secret_key()
        req = top.api.AlibabaAliqinFcSmsNumSendRequest(url)
        req.set_app_info(top.appinfo(appkey, secret))

        req.sms_type = "normal"
        req.sms_free_sign_name = cls.conf_loader.get_sign_name()
        req.sms_param = """{"system_name":"%s","exception_name":"%s","key_prompt":"%s"}""" % (system_name,exception_name,key_prompt)
        req.rec_num = cls.conf_loader.get_phone_num()
        req.sms_template_code = cls.conf_loader.get_sms_template_code()

        try:
            resp = req.getResponse()
            print(resp)
        except Exception as e:
            traceback.print_exc()

