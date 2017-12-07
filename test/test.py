# -*- coding: utf-8 -*-
from selenium import webdriver
import time
print(time.time())
service_args=[]
# service_args.append('--load-images=no')  ##关闭图片加载
# service_args.append('--disk-cache=yes')  ##开启缓存
# service_args.append('--ignore-ssl-errors=true') ##忽略https错误

# browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs', service_args=service_args)
browser = webdriver.PhantomJS('/Users/xhw/PythonU/phantomjs-2.1.1-macosx/bin/phantomjs')
browser.implicitly_wait(10)        ##设置超时时间
browser.set_page_load_timeout(10)  ##设置超时时间


browser.get('https://work.bugtags.com/login.html')
# user_name = browser.find_element_by_id('login_email')
# user_name.send_keys('1982700252@qq.com')
# user_id = browser.find_element_by_id('login_pwd')
# user_id.send_keys('Zx.666555')
#
#
# btn = browser.find_element_by_id('btn_login')
# btn.click()

time.sleep(1)

print(browser.page_source)

# print(browser.find_element_by_class_name('c-flag-0').get_attribute('class'))

browser.get('about:blank') #爬坑: 一次请求完 重置状态
print(time.time())

browser.close()     #close关闭当前页面

browser.quit()    #quit退出浏览器