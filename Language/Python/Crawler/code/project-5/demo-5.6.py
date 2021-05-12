# TODO: 关闭证书验证  <08-05-21, Redari-Es> #
import urllib.request
import ssl
# 关闭证书验证
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://kyfw.12306.cn/otn/leftTicket/init'
response = urllib.request.urlopen(url)
# 状态码
print(response.getcode())
