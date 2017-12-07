# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())

option = webdriver.FirefoxOptions()
option.add_argument("-headless")

browser = webdriver.Firefox(options=option)
browser.set_window_size(800, 800)
browser.set_page_load_timeout(10)  ##设置超时时间


browser.get("http://devdoc.xiaoyouapp.cn/publics/apiList")


# print(browser.page_source)

print(time.time())


browser.quit()    #quit退出浏览器