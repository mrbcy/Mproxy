# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JokeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    joke_id =scrapy.Field()
    user_name = scrapy.Field()
    up_vote_num = scrapy.Field()
    down_vote_num = scrapy.Field()
    comment_num = scrapy.Field()
    joke_text = scrapy.Field()