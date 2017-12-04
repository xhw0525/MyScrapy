# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
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


#----------------------------------------------------------------------------------------------------------------------



#下载中间件
# class MyCustomDownloaderMiddleware(object):
#     @classmethod
#     def process_request(cls, request, spider):
#         if request.meta.has_key('PhantomJS'):
#             print '-------->>>>>>>>>>>MyCustomDownloaderMiddleware----------->>>>>process_request'
#             service_args = []
#             service_args.append('--load-images=no')  ##关闭图片加载
#             # service_args.append('--disk-cache=yes')  ##开启缓存
#             service_args.append('--ignore-ssl-errors=true')  ##忽略https错误
#             browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs',
#                                           service_args=service_args)
#             browser.implicitly_wait(3)  ##设置超时时间
#             browser.set_page_load_timeout(3)  ##设置超时时间
#
#
#             browser.get(request.url)
#             # 妹的 browser好像只提供获取源代码的属性  无法得到js执行过后的html?
#             content = browser.page_source.encode('utf-8')
#
#             # browser.get('about:blank')  # 爬坑: 重用时, 一次请求完 重置状态
#             browser.close()
#             browser.quit()
#             # return Response(request.url, body=content, request=request)
#
#             return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
#
#         else:
#             return None

