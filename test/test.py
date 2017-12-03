# -*- coding: utf-8 -*-
from selenium import webdriver

browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs')
browser.get('https://www.baidu.com')
print (browser.file_detector_context)
browser.quit()