# -*- coding: utf-8 -*-
import scrapy
from MyScrapy.items import ImageaItem
from MyScrapy.webdrivers import Webdriver
from scrapy import Request

class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['douyu.com']
    start_urls = ['http://www.budejie.com/pic', ]

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
            item['img_url'] = img.extract()

            if item['img_url'].startswith('http') and \
                    (item['img_url'].endswith('jpeg') or
                         item['img_url'].endswith('jpg') or
                         item['img_url'].endswith('gif') or
                         item['img_url'].endswith('png')):
                yield item

    @staticmethod
    def close(spider, reason):
        Webdriver.close()
        return scrapy.Spider.close(spider, reason)
