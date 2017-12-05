# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import scrapy
import time
from scrapy.http import Response


class MyscrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# ----------------------------------------------------------------------------------------------------------------------
# 全局使用一个brower不知道会不会有问题?

option = webdriver.FirefoxOptions()
option.add_argument("-headless")
browser = webdriver.Firefox(options=option)
browser.set_window_size(1200, 800)
browser.implicitly_wait(5)  ##设置超时时间
browser.set_page_load_timeout(5)  ##设置超时时间

# 下载中间件
class MyCustomDownloaderMiddleware(object):

    @classmethod
    def process_request(cls, request, spider):

        if request.meta.has_key('Firefox'):
            global browser

            browser.get(request.url)
            content = browser.page_source.encode('utf-8')
            # browser.get('about:blank')  # 爬坑: 重用时, 一次请求完 重置状态
            browser.close()
            # cls.browser.quit()
            # return Response(request.url, body=content, request=request)
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        else:
            return None  # 返回 None, 交给下一个中间件  或者loader 处理

        #上面process_request的 response 不从这个方法过?
        def process_response(request, response, spider):
            yield response

