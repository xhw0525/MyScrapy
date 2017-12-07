
// 哈哈 浏览器也可以 无界面
option = webdriver.FirefoxOptions()
option.add_argument("--headless")

//滑到底部
js="var q=document.documentElement.scrollTop += document.body.scrollHeight"
//或者
js="var q=document.getElementById('节点id').scrollTop += document.getElementById('节点id').scrollHeight"

browser.execute_script(js)

# 全局使用一个brower不知道会不会有问题?
# option = webdriver.FirefoxOptions()
# option.add_argument("-headless")
# browser = webdriver.Firefox(options=option)
# browser.set_window_size(1200, 800)
# browser.implicitly_wait(5)  ##设置超时时间
# browser.set_page_load_timeout(5)  ##设置超时时间



# browser.get('about:blank')  # 爬坑: PhantomJS重用时, 一次请求完 重置状态
# browser.close(); <or> browser.quit();
#


selenium firefox46.0.1设置禁用图片
 firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)#某些firefox只需要这个
firefox_profile.set_preference('browser.migration.version', 9001)#部分需要加上这个
禁用css
firefox_profile.set_preference('permissions.default.stylesheet', 2)
禁用flash
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
禁用js
firefox_profile.set_preference('javascript.enabled', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://re.jd.com/'）