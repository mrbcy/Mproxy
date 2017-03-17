#-*- coding: utf-8 -*-
from mail.emailutil import EmailUtil
from sms.smsutil import SmsUtil
from task.availablecounttask import AvailableCountTask
from task.validatechecktask import ValidateCheckTask


def func():
    validate_check_task = ValidateCheckTask()
    validate_check_task.start()

    available_count_check_task = AvailableCountTask()
    available_count_check_task.start()
    # SmsUtil.send_sms('Mproxy','代理服务器数量已经告急，数量严重不足','200')
    # EmailUtil.send_email('代理服务器数量不足','测试异常信息')


if __name__ == '__main__':
    func()