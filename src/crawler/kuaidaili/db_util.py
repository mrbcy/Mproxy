#-*- coding: utf-8 -*-
import traceback

from mongoengine import *
import re

# connect to mongodb
connect('mproxy')


class ProxySegment(Document):
    ip = StringField(required=True)
    port = IntField(required=True)
    safety = StringField(max_length=20)
    type = StringField(max_length=20)
    location = StringField(max_length=50)


def save_proxy_segments(proxy_list):
    for p in proxy_list:
        try:
            regex_str = "\.".join(p['ip'].split('.')[:-1]) + "\.\d"
            # print(regex_str)
            regex = re.compile(regex_str)
            if len(ProxySegment.objects(ip=regex)) == 0:
                ProxySegment(ip=p['ip'], port=p['port'], safety=p['safety'], type=p['type'], location=p['location']).save()
        except Exception:
            traceback.print_exc()

