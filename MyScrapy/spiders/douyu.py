# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from MyScrapy.webdrivers import Webdriver
from MyScrapy.items import ImageaItem
import mybasespider

class DouyuSpider(mybasespider.WebdriverSpider):
    name = 'douyu'
    # allowed_domains = ['douyu.cn']
    start_urls = ['https://www.douyu.com/directory/game/yz']


    def parse(self, response):
        imgs_parents = response.xpath('//body/div[2]/div[3]/div[1]/div/div/div[3]/ul/li')

        for imgs_parent in imgs_parents:
            imgs = imgs_parent.xpath('a/span/img')

            if len(imgs) > 0:
                item = ImageaItem()
                item['name'] = imgs[0].xpath('@alt').extract()[0].encode('utf-8')
                item['img_url'] = imgs[0].xpath('@data-original').extract()[0]
                yield item

