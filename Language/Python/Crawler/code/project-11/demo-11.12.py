#将字典格式写入
URL='http://httpbin.org/post'
data={'key':'python'}
async with ClientSession() as session:
    async with session.post(URL,data=data) as response:
        response=await response.text()
        print(response)

#以json格式写入
URL='http://httpbin.org/post'
data={'key':'python'}
async with ClientSession() as session:
    async with session.post(URL,json=data) as response:
        response=await response.text()
        print(response)
#以字符串格式写入
URL='http://httpbin.org/post'
data='python'
async with ClientSession() as session:
    async with session.post(URL,data=data) as response:
        response=await response.text()
        print(response)


#设置编码格式
response=await response.text(encoding='utf-8')
#以字节流格式返回
response=await response.read()
#以json格式返回
response=await response.json()
#获取响应状态码
status=response.status
#获取响应的请求头
headers=response.headers
#获取URL地址
url=response.url
