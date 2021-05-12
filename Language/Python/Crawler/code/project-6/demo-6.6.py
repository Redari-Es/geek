import requests

url = 'https://movie.douban.com/'
r = requests.get(url)
print(r.cookies)
mycookies = r.cookies
#RequestsCookieJar转换字典
cookies_dict = requests.utils.dict_from_cookiejar(mycookies)
f = open('cookies.txt', 'w', encoding='utf-8')
f.write(str(cookies_dict))
f.close()
#读取文件
f = open('cookies.txt', 'r')
dict_values = f.read()
f.close()
#eval(dict_values)将字符串转换为字典
print(eval(dict_values))
r = requests.get(url, cookies=eval(dict_values))
print(r.status_code)
