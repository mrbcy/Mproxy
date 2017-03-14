#-*- coding: utf-8 -*-
import json
import traceback

from kafka import KafkaConsumer

from conf.configloader import ConfigLoader
from service.proxyservice import ProxyService
from validationresultitem import ValidationResultItem

validate_result = {}
validator_list = []
proxy_service = ProxyService()

def print_validator_names():
    global validator_list
    config_loader = ConfigLoader()
    validator_list = config_loader.get_validator_list()
    print validator_list

def do_validation_match(proxy_task):
    global validate_result
    try:
        if validate_result.has_key(proxy_task['task_id']) == False:
            validate_result[proxy_task['task_id']] = [ValidationResultItem(proxy_task)]
        else:
            validate_result[proxy_task['task_id']].append(ValidationResultItem(proxy_task))

        check_validation_result(proxy_task['task_id'])
    except Exception as e:
        traceback.print_exc()
        pass


def deal_unavailable(result_list):
    global proxy_service
    if len(result_list) > 0:
        print "代理服务器 %s:%s 不能用" %(result_list[0].ip,result_list[0].port)
        dao_item = proxy_service.find_proxy_by_addr(result_list[0].ip + ':'+result_list[0].port)
        if dao_item is not None:
            proxy_service.save_proxy(result_list[0])



def deal_available(result_list):
    global proxy_service
    if len(result_list) > 0:
        print "代理服务器 %s:%s 可用" % (result_list[0].ip, result_list[0].port)
        proxy_service.save_proxy(result_list[0])



def check_validation_result(task_id):
    global validate_result
    global validator_list
    # print validate_result[task_id]
    result_list = validate_result[task_id]

    # iteratively check whether proxy passes all the validators
    all_pass_flag = True
    for validator in validator_list:
        pass_flag = False
        for result_item in result_list:
            if validator == result_item.validator_name:
                pass_flag = True
                if result_item.validate_result == False:
                    print "根据 %s 判定，代理服务器不能用" % result_item.validator_name
                    deal_unavailable(result_list)
                    return
                break
        if pass_flag == False:
            all_pass_flag = False
    if all_pass_flag == True:
        deal_available(result_list)




def func():
    consumer = KafkaConsumer('checked-servers',
                             group_id='mproxy_collector',
                             bootstrap_servers=['amaster:9092','anode1:9092','anode2:9092'],
                             auto_offset_reset='earliest',
                             # enable_auto_commit=False,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    for message in consumer:
        v = message.value
        do_validation_match(v)


if __name__ == '__main__':
    print_validator_names()
    func()