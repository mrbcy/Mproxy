import scrapy
from scrapy import FormRequest
from scrapy.selector import HtmlXPathSelector

from joke.items import JokeItem


class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "xiaohua"
    allowed_domains = ["xiaohua.com"]
    download_delay = 2
    start_urls = [
        "http://xiaohua.com/Index/index/type/1.html",
    ]

    def parse(self, response):

        items = response.xpath('''//div[@class='one-cont']''')

        for item_selector in items:
            # go on to get elements
            user_name = item_selector.xpath('''.//div[@class='one-cont-font clearfix']/i/text()''').extract_first()
            up_vote_num = item_selector.xpath('''.//li[@class='active zan range']/span/text()''').extract_first()
            down_vote_num = item_selector.xpath('''.//li[@class='range cai']/span/text()''').extract_first()
            comment_num = item_selector.xpath('''.//li[@class='range jxi']/span/text()''').extract_first()
            joke_text = item_selector.xpath('''.//p[@class='fonts']/a/text()''').extract_first()
            joke_text = joke_text.strip() + '\n'
            joke_id = item_selector.xpath('''.//p[@class='fonts']/a/@href''').extract_first()
            joke_id = joke_id.replace('/Index/pinlun/id/','')
            joke_id = joke_id.replace('/type/1.html','')

            # data_list = [joke_id,user_name,up_vote_num,down_vote_num,comment_num]
            # print('\t'.join(data_list))
            # print(joke_text)
            item = JokeItem()
            item['joke_id'] = joke_id
            item['user_name'] = user_name
            item['up_vote_num'] = up_vote_num
            item['down_vote_num'] = down_vote_num
            item['comment_num'] = comment_num
            item['joke_text'] = joke_text
            print(type(item))
            yield item

        # recursively get more jokes
        more_url = 'http://xiaohua.com/index/more'
        yield FormRequest(url=more_url,
                          dont_filter=True,
                          formdata={'type': '1'},
                          callback=self.parse)
