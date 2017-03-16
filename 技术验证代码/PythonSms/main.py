#-*- coding: utf-8 -*-
import traceback

import top.api

def func():
    url = "gw.api.taobao.com"
    appkey = ""
    secret = ""
    req = top.api.AlibabaAliqinFcSmsNumSendRequest(url)
    req.set_app_info(top.appinfo(appkey, secret))

    req.sms_type = "normal"
    req.sms_free_sign_name = ""
    req.sms_param = """{"system_name":"Mproxy","exception_name":"代理服务器数量不足","key_prompt":"1958"}"""
    req.rec_num = ""
    req.sms_template_code = ""
    try:
        resp = req.getResponse()
        print(resp)
    except Exception, e:
        traceback.print_exc()


if __name__ == '__main__':
    func()