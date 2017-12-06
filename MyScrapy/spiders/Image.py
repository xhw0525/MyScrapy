# -*- coding: utf-8 -*-
import scrapy
from MyScrapy.items import ImageaItem
from MyScrapy.webdrivers import Webdriver
from scrapy import Request

class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['douyu.com']
    start_urls = ['http://www.budejie.com/pic',]
    def start_requests(self):
        for url in self.start_urls:
            request = Request(url)
            request.meta['Firefox'] = True
            yield request

    def parse(self, response):
        images = response.xpath('//img/@src')
        for img in images:
            item = ImageaItem()
            item['name'] = ""
            item['url'] = img.extract()
            if item['url'].startswith('http') and (item['url'].endswith('jpeg') or item['url'].endswith('jpg') or item['url'].endswith('png')):
                yield item

    @staticmethod
    def close(spider, reason):
        Webdriver.close()
        return scrapy.Spider.close(spider, reason)