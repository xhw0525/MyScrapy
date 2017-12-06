# -*- coding: utf-8 -*-
from selenium import webdriver

# 全局使用一个brower不知道会不会有问题? -------tmd
# 貌似scrapy 的 download 和 parse 都是是在单一线程完成的
# 那到底哪里是多线程并发啊啊啊?????exit
## 待优化

class Webdriver(object):

    __webdriver = None

    def __init__(self):
        option = webdriver.FirefoxOptions()
        option.add_argument("-headless")
        self.browser = webdriver.Firefox(options=option)
        self.browser.set_window_size(800, 800)
        self.browser.implicitly_wait(5)  ##设置超时时间
        self.browser.set_page_load_timeout(5)  ##设置超时时间

    @staticmethod
    def get_instance():
        if Webdriver.__webdriver is None:
            Webdriver.__webdriver = Webdriver()
        return Webdriver.__webdriver

    @staticmethod
    def close():
        if Webdriver.__webdriver is not None:
            Webdriver.__webdriver.browser.quit()
