# -*- coding: utf-8 -*-
import scrapy
from MyScrapy.items import ImageaItem


class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['douyu.com']
    start_urls = ['http://www.budejie.com/pic',]

    def parse(self, response):
        images = response.xpath('//img/@src')
        for img in images:
            item = ImageaItem()
            item['name'] = ""
            item['url'] = img.extract()
            yield item
