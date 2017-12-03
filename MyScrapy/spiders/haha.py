# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from MyScrapy.items import MyscrapyItem


class HahaSpider(scrapy.Spider):
    name = 'haha'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com']

    def parse(self, response):

        print('--可根据url做一些事情--'+response.url)

        lista = response.xpath("//a")
        for alink in lista:
            item = MyscrapyItem()
            item['a'] = alink.extract()
            item['name'] = alink.extract()
            yield item
            # yield Request("http://hahahahfah.com", callback=self.parse)