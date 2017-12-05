# -*- coding: utf-8 -*-
from selenium import webdriver

# 全局使用一个brower不知道会不会有问题? -------tmd
# 貌似scrapy 的 download 和 parse 都是是在单一线程完成的
# 那到底哪里是多线程并发啊啊啊?????

option = webdriver.FirefoxOptions()
option.add_argument("-headless")
instance = webdriver.Firefox(options=option)
instance.set_window_size(800, 800)
instance.implicitly_wait(5)  ##设置超时时间
instance.set_page_load_timeout(5)  ##设置超时时间