import urllib.request
from http import cookiejar

filename = 'cookie.txt'
# 创建MozillaCookieJar对象
cookie = cookiejar.MozillaCookieJar()
# 读取cookie内容到变量
cookie.load(filename)
# HTTPCookieProcessor创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建opener
opener = urllib.request.build_opener(handler)
# 打开
response = opener.open('https://movie.douban.com/')
# 输出结果
print(cookie)

# 使cookies信息隐藏在文件中
cookie.save(ignore_discard=True, ignore_expires=True)
cookie.load(filename, ignore_discard=True, ignore_expires=True)
