# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())


browser = webdriver.Safari()
# browser.implicitly_wait(10)        ##设置超时时间
# browser.set_page_load_timeout(10)  ##设置超时时间


browser.get("http://devdoc.xiaoyouapp.cn/publics/apiList")


# print(browser.page_source)

# print(browser.find_element_by_class_name('c-flag-0').get_attribute('class'))

# browser.get('about:blank') #爬坑: 一次请求完 重置状态
print(time.time())

# browser.close()     #close关闭当前页面

browser.quit()    #quit退出浏览器