#-*- coding: utf-8 -*-
import json

from kafka import KafkaConsumer


def func():


    consumer = KafkaConsumer('json-topic',
                             group_id='group3',
                             bootstrap_servers=['amaster:9092'],
                             auto_offset_reset='earliest', enable_auto_commit=False,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))


    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        # proxyData = json.loads(message.value.decode('utf-8'))
        # line = ("IP：%(ip)s 端口号：%(port)s 匿名度：%(anonymity)s 类型：%(type)s 位置：%(location)s") % message.value
        print message.value

if __name__ == '__main__':
    func()