#导入urllib
import urllib.request

url = 'https://movie.douban.com/'
# 自定义请求头
headers = {
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive'
}
# 设置request请求头
req = urllib.request.Request(url, headers=headers)
#使用urlopen打开req
html = urllib.request.urlopen(req).read().decode('utf-8')

#写入文件
f = open('html.txt', 'w', encoding='utf8')
f.write(html)
f.close()
