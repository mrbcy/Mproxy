#-*- coding: utf-8 -*-
import logging
import time
from logging.handlers import RotatingFileHandler


def func():
    init_log()
    while True:
        print "output to the console"
        logging.debug("output the debug log")
        logging.info("output the info log")
        time.sleep(3);


def init_log():
    logging.getLogger().setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

    # add log ratate
    Rthandler = RotatingFileHandler("backend_run.log", maxBytes=10 * 1024 * 1024, backupCount=100,
                                    encoding="gbk")
    Rthandler.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    Rthandler.setFormatter(formatter)
    logging.getLogger().addHandler(Rthandler)



if __name__ == '__main__':
    func()