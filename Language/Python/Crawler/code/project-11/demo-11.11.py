import aiohttp
#不带参数
URL='http://httpbin.org/get'
async with ClientSession() as response:
    async with session.get(URL) as response:
        response=await response.text()
        print(response)
#带参数
#在URL设置参数
URL='http://httpbin.org/get?key=python'
async with ClientSession() as session:
    async with session.get(URL) as response:
        response =await response.text()
        print(response)

#设置请求参数params
URL='http://httpbin.org/get'
params={'wd':'python'}
async with ClientSession() as session:
    async with session.get(URL,params=params) as response:
        response=await response.text()
        print(response)
