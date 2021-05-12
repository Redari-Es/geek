from aiohttp import ClientSession
import aiohttp
URL='http://httpbin.org'
#设置请求头
headers={'content-type':'application/json'}
async with ClientSession(headers=headers) as session:
    async with session.get(URL,headers=headers) as response:
        response=await response.text()
#设置超时，在会话中设置超时
timeout = aiohttp.ClientTimeout(total=60)
async with ClientSession(timeout=timeout) as session:
    async with session.get(URL) as response:
        response = await response.text()
        print(response)
#设置超时，在请求中设置超时
async with ClientSession() as session:
    async with session.get(URL,timeout=timeout) as response:
        response = await response.text()
        print(response)

#设置cookies
cookies={'cookies':'working'}
async with ClientSession(cookies=cookies) as session:
    async with session.get(URL) as respons:
        response=await response.text()
        print(response)

        #设置代理IP
proxy='http://117.191.11.72:8080'
async with ClientSession() as session:
    async with session.get(URL,proxy=proxy) as response:
        response=await response.text()
        print(response)
#支持代理授权
async with ClientSession() as session:
    proxy_auth=aiohttp.BasicAuth('user','pass')
    async with session.get("http://python.org",
                           proxy="http://proxy.com",
                           proxy_auth=proxy_auth) as resp:
        response=await response.text()
        print(response)

