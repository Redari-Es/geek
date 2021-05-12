# TODO: 代理ip  <08-05-21, Redari-Es> #
import urllib.request

url = 'https://movie.douban.com/'
#设置代理ip
proxy_handler = urllib.request.ProxyHandler({
    'http': '218.56.132.157:8080',
    'https': '183.30.197.29:9797'
})
# 必须使用build_opener()函数来创建带有自代理IP功能的opener对象
opener = urllib.request.build_opener(proxy_handler)
response = opener.open(url)
html = response.read().decode('utf-8')
f = open('html3.txt', 'w', encoding='utf8')
f.write(html)
f.close()
## 代理ip的问题，成功需要更换
