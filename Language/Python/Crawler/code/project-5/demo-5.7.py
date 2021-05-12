# TODO: 数据处理  <08-05-21, Redari-Es> #
import urllib.request
import urllib.parse

url = 'https://movie.douban.com/'
headers = {
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Referer': 'https://movie.douban.com/',
    'Connection': 'keep-alive'
}
data = {'value': 'true'}
# 数据处理
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.urlopen(url, data=data)
