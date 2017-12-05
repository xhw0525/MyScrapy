# -*- coding: utf-8 -*-
import scrapy


class DouyuSpider(scrapy.Spider):
    name = 'DouYu'
    allowed_domains = ['http://douyu.com']
    start_urls = ['http://http://douyu.com/']

    def parse(self, response):
        pass
