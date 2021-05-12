from selenium import webdriver

url = 'https://movie.douban.com/'
driver = webdriver.Chrome()
driver.get(url)
#定位
driver.find_element_by_id('inp-query').send_keys('红海行动')
driver.find_element_by_name('search_text').send_keys('我不是药神')
