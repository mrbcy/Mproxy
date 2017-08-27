#-*- coding: utf-8 -*-

"http://www.xicidaili.com/nn/1"
import random
import traceback

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from util.db_util import *


def get_proxies(pages):
    base_url = 'http://www.xicidaili.com/nn/'
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(20)
    for i in range(880, pages):
        url = base_url + str(i)
        driver.get(url)
        # 提取代理地址
        bs = BeautifulSoup(driver.page_source, "lxml")
        proxy_list = bs.find_all("tr")[1:]
        # print(proxy_list)

        proxies = []
        for proxy in proxy_list:
            try:
                tds = proxy.find_all("td")[1:6]
                # print(tds)
                ip = tds[0].get_text()
                port = tds[1].get_text()
                safety = tds[3].get_text()
                if safety == '高匿':
                    safety = '高匿名'
                proxy_type = tds[4].get_text()
                location = "未知"
                if len(list(tds[2].contents)) > 2:
                    location = list(tds[2].contents)[1].string
                proxies.append({"ip": ip, "port": port, "safety": safety, "type": proxy_type, "location": location, "source": "xicidaili"})
            except Exception:
                traceback.print_exc()
        # print(proxies)
        save_proxy_segments(proxies)
        sleep_time = random.randint(1, 2)
        print("保存第 " + str(i) + " 页数据成功, 休息" + str(sleep_time) + "s")
        time.sleep(sleep_time)
    print("save all proxies to mongodb")

if __name__ == '__main__':
    get_proxies(2309)