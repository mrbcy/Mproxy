#-*- coding: utf-8 -*-
import random
import traceback

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from util.db_util import *


def get_proxies(pages):
    base_url = 'http://www.kuaidaili.com/free/inha/'
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(20)
    for i in range(1, pages):
        url = base_url + str(i) + '/'
        driver.get(url)
        # 提取代理地址
        bs = BeautifulSoup(driver.page_source, "lxml")
        proxy_list = bs.find_all("tr")[1:]
        # print(proxy_list)
        proxies = []
        for proxy in proxy_list:
            try:
                ip = proxy.find("td", {"data-title": "IP"}).get_text()
                port = int(proxy.find("td", {"data-title": "PORT"}).get_text())
                safety = proxy.find("td", {"data-title": "匿名度"}).get_text()
                proxy_type = proxy.find("td", {"data-title": "类型"}).get_text()
                location = proxy.find("td", {"data-title": "位置"}).get_text()
                proxies.append({"ip": ip, "port": port, "safety": safety, "type": proxy_type, "location": location})
            except Exception:
                traceback.print_exc()
        save_proxy_segments(proxies)
        sleep_time = random.randint(1, 4)
        print("保存第 " + str(i) + " 页数据成功, 休息" + str(sleep_time) + "s")
        time.sleep(sleep_time)
    print("save all proxies to mongodb")

if __name__ == '__main__':
    get_proxies(1777)
