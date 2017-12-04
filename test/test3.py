# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())
service_args=[]

service_args.append('--load-images=no')  ##关闭图片加载
# service_args.append('--disk-cache=yes')  ##开启缓存
service_args.append('--ignore-ssl-errors=true') ##忽略https错误

browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs', service_args=service_args)
browser.implicitly_wait(10)        ##设置超时时间
browser.set_page_load_timeout(10)  ##设置超时时间
browser.set_window_size(800, 800)

browser.get('http://devdoc.xiaoyouapp.cn/publics/apiList')
# time.sleep(3)

# browser.save_screenshot('截图.png')

list = browser.find_elements_by_css_selector('div')
for li in list:
    print li.text

# print(browser.find_element_by_class_name('c-flag-0').get_attribute('class'))

browser.get('about:blank') #爬坑: 一次请求完 重置状态
print(time.time())

browser.close()     #close关闭当前页面

browser.quit()    #quit退出浏览器