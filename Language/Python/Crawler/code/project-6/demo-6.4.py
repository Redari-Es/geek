# cookie
import requests

temp_cookies = 'JSESSIONID_GDS=y4p7osFr_IYV5Udyd6c1drWE8MeTpQn0Y58Tg8cCCONVP020y2N!!!450649273;name=value'
cookies_dict = {}
for i in temp_cookies.split(';'):
    value = i.split('=')
    cookies_dict[value[0]] = value[1]
r = requests.get(url, cookies=cookies_dict)
print(r.text)