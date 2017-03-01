#-*- coding: utf-8 -*-
import logging
import uuid
from logging.handlers import RotatingFileHandler

import sys
reload(sys)
sys.setdefaultencoding('gbk')

import scrapy
from scrapy_splash import SplashRequest

from kuaidaili.items import KuaidailiItem


class KuaidailiSpider(scrapy.spiders.Spider):
    name = "kuaidaili"
    allowed_domains = ["kuaidaili.com"]
    download_delay = 1
    start_urls = []

    def __init__(self):
        for x in range(10):
            self.start_urls.append('http://www.kuaidaili.com/proxylist/%d/' % (x+1))

        # self.start_urls.append('http://www.baidu.com')

        self.headers = {
            "Host": "www.kuaidaili.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://onlinelibrary.wiley.com/journal/10.1002/(ISSN)1521-3773",
            "Cookie": "_gat=1; channelid=0; sid=1488211261856538; _ga=GA1.2.167063512.1488083088; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1488083088,1488174082,1488205850,1488211463; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1488211463",
            "Connection": "keep-alive",
            "Upgrade - Insecure - Requests": "1"
        }
        self.init_log()

    def init_log(self):
        # add log ratate
        Rthandler = RotatingFileHandler('kuaidaili_spider.log', maxBytes=10 * 1024 * 1024, backupCount=100,encoding = "gbk")
        Rthandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        Rthandler.setFormatter(formatter)
        logging.getLogger().addHandler(Rthandler)

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield SplashRequest(url, self.parse, args={'wait': 1})

    def parse(self, response):
        try:
            trs = response.xpath('''//*[@id="index_free_list"]/table/tbody/tr''')
            for tr_selector in trs:
                item = KuaidailiItem()
                item['ip'] = tr_selector.xpath('''./td[1]/text()''').extract_first()
                item['port'] = tr_selector.xpath('''./td[2]/text()''').extract_first()
                item['anonymity'] = tr_selector.xpath('''./td[3]/text()''').extract_first()
                item['type'] = tr_selector.xpath('''./td[4]/text()''').extract_first()
                item['location'] = tr_selector.xpath('''./td[6]/text()''').extract_first()
                item['task_id'] = str(uuid.uuid4())

                yield item
        except Exception as e:
            logging.exception("An Error Happens")


