from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://movie.douban.com/'
#Options类实例化
chrome_options = Options()
#设置浏览器参数
#--headless是不显示浏览器启动以及执行过程
chrome_options.add_argument('--headless')
#设置lang和user-agent信息，防止反爬虫检测
chrome_options.add_argument('lang=zh_CN.UTF-8')
UserAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
chrome_options.add_argument('User-Agent' + UserAgent)
#启动浏览器并设置chrome_options参数
driver = webdriver.Chrome(chrome_options=chrome_options)
#浏览器窗口最大化
driver.maximize_window()
#浏览器窗口最小化
driver.minimize_window()
driver.get(url)
#获取网页的标题内容
print(driver.title)
#page_source是获取网页的HTML代码
print(driver.page_source)
