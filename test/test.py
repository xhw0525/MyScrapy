# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())
service_args=[]
# service_args.append('--load-images=no')  ##关闭图片加载
# service_args.append('--disk-cache=yes')  ##开启缓存
# service_args.append('--ignore-ssl-errors=true') ##忽略https错误

browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs', service_args=service_args)
browser.implicitly_wait(10)        ##设置超时时间
browser.set_page_load_timeout(10)  ##设置超时时间
browser.set_window_size(800, 1900) ##截图区域 还是 显示区域?

browser.get('https://www.baidu.com')
browser.save_screenshot("codingpy.png") ## 截图

print (browser.title)
browser.get('about:blank') #爬坑: 一次请求完 重置状态
print(time.time())

browser.close()     #close关闭当前页面

browser.quit()    #quit退出浏览器