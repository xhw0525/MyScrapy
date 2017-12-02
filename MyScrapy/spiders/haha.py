# -*- coding: utf-8 -*-
import scrapy
from MyScrapy.items import MyscrapyItem


class HahaSpider(scrapy.Spider):
    name = 'haha'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        lista = response.xpath("//a")

        for a in lista:
            item = MyscrapyItem()
            item["a"] = a.extract().encode("utf-8")
            yield item
