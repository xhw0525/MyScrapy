# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from MyScrapy.items import JieKouItem
from MyScrapy.webdrivers import Webdriver


class JiekouSpider(scrapy.Spider):
    name = 'JieKou'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://devdoc.xiaoyouapp.cn/publics/apiList']

    def start_requests(self):
        for url in self.start_urls:
            request = Request(url)
            request.meta['Firefox'] = True
            yield request

    def parse(self, response):

        print('--可根据url做一些事情--' + response.url)


        lista = response.xpath("/html/body/div[2]/div/div[1]/div")

        for a in lista:
            if a.xpath('div[2]/a/h5') and a.xpath('div[1]/h5/span') and a.xpath('div[2]/a/h5/text()').extract()[0].startswith('http'):

                print '------->>>>>>>', a.xpath('div[1]/h5/span/text()').extract()[0].encode('utf-8')
                print '------->>>>>>>', a.xpath('div[2]/a/h5/text()').extract()[0]

    @staticmethod
    def close(spider, reason):
        Webdriver.close()
        return scrapy.Spider.close(spider, reason)