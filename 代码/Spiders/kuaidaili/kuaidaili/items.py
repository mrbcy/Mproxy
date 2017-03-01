# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KuaidailiItem(scrapy.Item):
    task_id = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    anonymity = scrapy.Field()
    type = scrapy.Field()
    location = scrapy.Field()

