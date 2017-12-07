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
time.sleep(1)
js="var q=document.getElementById('mainbody').scrollTop = document.getElementById('mainbody').scrollHeight * 0.1"
browser.execute_script(js)

time.sleep(1)

print(browser.find_element_by_id('mainbody'))

browser.save_screenshot('hahahaha.png')



browser.quit()    #quit退出浏览器
print(time.time())
