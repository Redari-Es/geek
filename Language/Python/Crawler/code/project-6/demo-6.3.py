# 证书验证
import requests

url = 'https://kyfw.12306.cn/otn/leftTicket/init'
# 关闭证书验证
r = requests.get(url, verify=False)
print(r.status_code)
#开启证书验证
#r=requests.get(url,verify=True)
#设置证书所在的路径
#r=requests.get(url, verify='/path/to/certfile')

#超时设置
requests.get("https://www.baidu.com/", timeout=0.001)
requests.post("https://www.baidu.com/", timeout=0.001)
