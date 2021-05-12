from requests_html import HTMLSession
# 定义会话session
session = HTMLSession()
url = 'https://movie.douban.com/'
#发送get请求
r = session.get(url)
#输出网页的URL地址
print(r.html)
#输出网页里全部URL地址
print(r.html.links)
#输出网页里的精准的URLdivi
print(r.html.absolute_links)
#输出网页的全部文本信息，即去除HTML代码
print(r.html.text)
