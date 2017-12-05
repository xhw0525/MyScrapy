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


browser.get("https://www.douyu.com/directory/game/yz")
browser.save_screenshot('hahahaha.png')

images = browser.find_elements_by_xpath('//ul/li/a/span/img')


for img in images:
    print '----->', img.get_attribute('data-original').encode('utf-8')

browser.quit()    #quit退出浏览器
print(time.time())
