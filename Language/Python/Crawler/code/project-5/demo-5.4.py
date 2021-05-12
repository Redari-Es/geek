# TODO: 使用cookies  <08-05-21, Redari-Es> #
import urllib.request
from http import cookiejar

filename = 'cookie.txt'
# MozillaCookieJar保存cookie
cookie = cookiejar.MozillaCookieJar(filename)
# HTTPCookieProcessor创建cookiee处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
# 创建自定义opener
response = opener.open('https://movie.douban.com/')
# 保存cookie文件
cookie.save()
#会被拒绝
