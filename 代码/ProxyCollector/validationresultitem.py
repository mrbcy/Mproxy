#-*- coding: utf-8 -*-

class ValidationResultItem:
    def __init__(self,validation_result):
        self.spider_name = validation_result['spider_name'].encode('utf-8')
        self.validator_name = validation_result['validator_name'].encode('utf-8')
        self.task_id = validation_result['task_id'].encode('utf-8')
        self.ip = validation_result['ip'].encode('utf-8')
        self.location = validation_result['location'].encode('utf-8')
        self.validate_result = validation_result['validate_result']
        self.anonymity = validation_result['anonymity'].encode('utf-8')
        self.type = validation_result['type'].encode('utf-8')
        self.port = validation_result['port'].encode('utf-8')

        if self.validate_result == True:
            print "验证器：%s 地址：%s:%s" % (self.validator_name,self.ip,self.port)
