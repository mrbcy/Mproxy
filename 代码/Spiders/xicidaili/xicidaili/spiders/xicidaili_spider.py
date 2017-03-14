# -*- coding: utf-8 -*-
import logging
import uuid
from logging.handlers import RotatingFileHandler

import scrapy
import sys
from scrapy_splash import SplashRequest

from xicidaili.conf.configloader import ConfigLoader
from xicidaili.items import XicidailiItem

reload(sys)
sys.setdefaultencoding('gbk')



class XicidailiSpider(scrapy.spiders.Spider):
    name = "xicidaili"
    allowed_domains = ["xicidaili.com"]
    download_delay = 1
    start_urls = []

    def __init__(self):
        self.conf_loader = ConfigLoader()
        for x in range(80):
            self.start_urls.append('http://www.xicidaili.com/nn/%d' % (x + 1))

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield SplashRequest(url, self.parse, args={'wait': 1})

    def init_log(self):
        # add log ratate
        Rthandler = RotatingFileHandler(self.conf_loader.get_log_file_name(), maxBytes=10 * 1024 * 1024,
                                        backupCount=100, encoding="gbk")
        Rthandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        Rthandler.setFormatter(formatter)
        logging.getLogger().addHandler(Rthandler)

    def parse(self, response):
        try:
            # //*[@id="ip_list"]/tbody/tr[2]/td[2]
            trs = response.xpath('''//*[@id="ip_list"]/tbody/tr[@class='odd']''')
            # print trs
            for tr_selector in trs:
                item = XicidailiItem()
                item['ip'] = tr_selector.xpath('''./td[2]/text()''').extract_first()
                item['port'] = tr_selector.xpath('''./td[3]/text()''').extract_first()
                item['location'] = tr_selector.xpath('''./td[4]/a/text()''').extract_first()
                if item['location'] is None:
                    item['location'] = "不明"
                item['anonymity'] = tr_selector.xpath('''./td[5]/text()''').extract_first()
                item['type'] = tr_selector.xpath('''./td[6]/text()''').extract_first()
                item['task_id'] = str(uuid.uuid4())
                item['spider_name'] = self.name
                yield item
        except Exception as e:
            logging.exception("An Error Happens")
