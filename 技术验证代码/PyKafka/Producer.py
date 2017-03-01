#-*- coding: utf-8 -*-
import json

from kafka import KafkaProducer


def func():
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                             bootstrap_servers=['amaster:9092','anode1:9092','anode2:9092'])
    for _ in range(100):
        producer.send('json-topic', {'ip': '117.90.1.130','port':'9000','anonymity':'高匿名','type':'HTTP,HTTPS','location':'中国 江苏省 镇江市 电信'})

    producer.close()




if __name__ == '__main__':
    func()