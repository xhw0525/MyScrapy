source ~/PythonU/bin/activate  进入python虚拟环境
source ~/PythonU/bin/activate; cd ~/PycharmProjects/MyScrapy;

#   scrapy startproject project_name
#   scrapy genspider [-t template] <name> <domain>
#   scrapy genspider haha www.baidu.com

crawl
scrapy crawl <spider>
使用spider进行抓取
scrapy crawl weather

check
scrapy check [-l] <spider>
运行contract检查

list
scrapy list
列出当前项目中所有可用的spider，每一行输出一个spider。

// 哈哈 浏览器也可以 无界面
option = webdriver.FirefoxOptions()
option.add_argument("--headless")



# 全局使用一个brower不知道会不会有问题?
# option = webdriver.FirefoxOptions()
# option.add_argument("-headless")
# browser = webdriver.Firefox(options=option)
# browser.set_window_size(1200, 800)
# browser.implicitly_wait(5)  ##设置超时时间
# browser.set_page_load_timeout(5)  ##设置超时时间



# browser.get('about:blank')  # 爬坑: PhantomJS重用时, 一次请求完 重置状态
# browser.close()
# cls.browser.quit()
# return Response(request.url, body=content, request=request)