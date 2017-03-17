#-*- coding: utf-8 -*-
from sms.smsutil import SmsUtil
from task.availablecounttask import AvailableCountTask
from task.validatechecktask import ValidateCheckTask


def func():
    validate_check_task = ValidateCheckTask()
    validate_check_task.start()

    available_count_check_task = AvailableCountTask()
    available_count_check_task.start()
    # SmsUtil.send_sms('Mproxy','代理服务器数量不足','200')


if __name__ == '__main__':
    func()