# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())


# ChromeOptions chromeOptions = new ChromeOptions();
# //        设置为 headless 模式 （必须）
#         chromeOptions.addArguments("--headless");
option = webdriver.FirefoxOptions()
option.add_argument("-headless")

browser = webdriver.Firefox(options=option)
browser.set_window_size(800, 800)
# browser.implicitly_wait(10)        ##设置超时时间
# browser.set_page_load_timeout(10)  ##设置超时时间


browser.get("http://devdoc.xiaoyouapp.cn/publics/apiList")


print(browser.page_source)

# print(browser.find_element_by_class_name('c-flag-0').get_attribute('class'))

# browser.get('about:blank') #爬坑: 一次请求完 重置状态
print(time.time())

# browser.close()     #close关闭当前页面

browser.quit()    #quit退出浏览器