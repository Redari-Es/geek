#导入Selenium的wedriver类
from selenium import webdriver
#设置变量url，用于访问
url = 'https://www.baidu.com/'
#将webdriver类实例化，将浏览器设定为goole
#参数executable_path是设置chromedriver的路径
path = '/usr/bin/chromedriver'
browser = webdriver.Chrome(executable_path=path)
browser.get(url)
'''
#启动火狐
from selenium import webdriver
browser=webdriver.Firefox()
browser.get(http://www.baidu.com/)

#启动IE
from selenium import webdriver
browser=webdriver.Ie()
browser.get('http://www.baidu.com/')

'''
