#-*- coding: utf-8 -*-

class TracebackContainer:
    def __init__(self):
        self.message = ""

    def write(self, str):
        '''
        把traceback信息存储必须的函数
        '''
        self.message += str