#-*- coding: utf-8 -*-
from conf.configloader import ConfigLoader


def func():
    conf_loader = ConfigLoader()
    print conf_loader.get_sign_name()


if __name__ == '__main__':
    func()