# -*- coding: utf-8 -*-
import scrapy


class JiekouSpider(scrapy.Spider):
    name = 'JieKou'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
