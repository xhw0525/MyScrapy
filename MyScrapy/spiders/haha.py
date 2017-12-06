# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from MyScrapy.webdrivers import Webdriver
from MyScrapy.items import MyscrapyItem


class HahaSpider(scrapy.Spider):

    name = 'haha'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com']

    def start_requests(self):
        for url in self.start_urls:
            request = Request(url)
            request.meta['Firefox'] = True
            yield request

    def parse(self, response):
        lista = response.xpath("//a")
        for alink in lista:
            item = MyscrapyItem()
            item['a'] = alink.xpath('@href').extract()[0]
            if alink.xpath('text()'):
                item['name'] = alink.xpath('text()').extract()[0]
            else:
                item['name'] = unicode('未获取到')

            yield item
            # yield Request("http://hahahahfah.com", callback=self.parse)

    @staticmethod
    def close(spider, reason):
        Webdriver.close()
        return scrapy.Spider.close(spider, reason)