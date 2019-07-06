# -*- coding: utf-8 -*-
import scrapy
from MyScrapy.spiders.mybasespider import WebdriverSpider

class BugtagsSpider(WebdriverSpider):
    name = 'bugtags'
    allowed_domains = ['bugtags']
    start_urls = ['http://bugtags/']

    def parse(self, response):
        pass
