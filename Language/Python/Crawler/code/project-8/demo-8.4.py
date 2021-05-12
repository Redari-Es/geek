from requests_html import HTMLSession
#定义会话
session = HTMLSession()
url = 'https://movie.douban.com/'
#发送get
r = session.get(url)
#通过CSS Selector定位li标签，".title"代表class属性
#first=True代表获取第一个元素
print(r.html.find('li.title', first=True).text)
#输出当前标签的属性值
print(r.html.find('li.title', first=True).attrs)
print('——————————分割线————————————')

#查找特定文本的元素
#如果元素所在的HTML里含有containing的属性值即可提取
for name in r.html.find('li', containing='超能'):
    #输出电影名
    print(name.text)
print('——————————分割线————————————')

#查找全部电影名
for name in r.html.find('li.title'):
    #输出电影名
    print(name.attrs)
print('——————————分割线————————————')

#通过xpath Selector定位ul标签，
x = r.html.xpath('//*[@id="screening"]/div[2]/ul')
for name in x:
    print(name.text)

print('——————————分割线————————————')
#seach()通过关键字查找内容
#一个{}代表一个内容，内容可为中文或英文等
print(r.html.search('古剑奇谭{}{}'))

print('——————————分割线————————————')
#search_all()通过关键字查找整个网页符合的内容
print(r.html.search_all('古剑奇谭{}{}'))
