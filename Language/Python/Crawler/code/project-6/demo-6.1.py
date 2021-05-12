import requests
# 第一种方式
r = requests.get('https://www.baidu.com/s?wd=python')
# 第二种方式
url = 'https://www.baidu.com/s'
params = {'wd': 'python'}
# 左边params在GET请求中表示设置参数
r = requests.get(url, params=params)
print(r.url)

## 建议使用第一种，比较简洁

# 字典类型
data = {'key1': 'value1', 'key2': 'value2'}
# 元组或列表
(('key1', 'value1'), ('key1', 'value2'))
# json
import json

data = {'key1': 'value1', 'key2': 'value2'}
# 将字典转换json
data = json.dumps(data)
# 发送post请求
r = requests.post("https://www.baidu.com/", data=data)
print('r.text')
