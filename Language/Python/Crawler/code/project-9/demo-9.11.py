from selenium import webdriver
import json, time
#百度用户登录并保存cookie
#url = 'https://passport.baidu.com/v2/'
#url = 'https://zhidao.baidu.com/'
url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
#driver.find_element_by_xpath('//*[@id="ul"]/a[7]').click()
driver.find_element_by_xpath('//*[@id="s-top-loginbtn"]').click()
#driver.find_element_by_xpath('//*[@id="userbar-login"]').click()

time.sleep(3)
driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
time.sleep(3)
#设置用户的帐号和密码
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys(
    '18823353886')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys(
    'hx905422030')

driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()
time.sleep(3)
"""
try:
    verifyCode = driver.find_element_by_name('verifyCode')
    code_number = input('请输入图片验证码:')
    verifyCode.send_keys(str(code_number))
except:
    pass
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
time.sleep(3)
try:
    driver.find_element_by_xpath(
        '//*[@id="TANGRAM__PSP__36__button_send_mobile"]').click()
    code_photo = input('请输入短信验证码：')
    driver.find_element_by_xpath(
        '//*[@id="TANGRAM__PSP__36__input_vcode"]').send_keys(str(code_photo))
    driver.find_element_by_xpath(
        '//*[@id="TANGRAM__PSP__36__button_submit"]').click()
    time.sleep(3)
except:
    pass
"""
cookies = driver.get_cookies()
f1 = open('~/Document/geek/Language/Python/Crawler/code/project-9/cookie.txt',
          'w')
f1.write(json.dumps(cookies))
f1.close()
