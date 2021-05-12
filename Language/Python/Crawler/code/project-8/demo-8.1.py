from requests_html import HTMLSession
# 定义会话Session
session = HTMLSession()
url = 'https://movie.douban.com/'

#发送get请求
r = session.get(url)
#发送post请求
r = session.post(url, data={})
print(r.html)
