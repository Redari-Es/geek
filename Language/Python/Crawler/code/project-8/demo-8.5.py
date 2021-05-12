from requests_html import HTMLSession

url = 'https://y.qq.com/portal/singer_list.html'
session = HTMLSession()
r = session.get(url)
#使用chromium浏览器加载网页
r.html.render()
#定位歌手姓名
singer = r.html.find('h3.singer_list__title')
#输出歌手名
for i in singer:
    print(i.text)
