# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())


browser = webdriver.Safari()
# browser.implicitly_wait(10)        ##设置超时时间
# browser.set_page_load_timeout(10)  ##设置超时时间


browser.get("https://www.douyu.com/directory/game/yz")


images = browser.find_elements_by_xpath('//ul/li/a/span/img')


for img in images:
    print '----->', img.get_attribute('data-original').encode('utf-8')

browser.quit()    #quit退出浏览器