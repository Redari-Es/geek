import requests

headers = {
    'UserAgent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
target_url = 'https://y.qq.com/portal/singer_list.html'

#render.html获取JS加载后的网页信息
url = 'http://0.0.0.0:8050/render.html?url=' + target_url + '&wait=5'
response = requests.get(url, headers=headers)
print(response.text)

#render.png获取网页截图
url = 'http://0.0.0.0:8050/render.png?url=' + target_url + '&wait=5'
response = requests.get(url, headers=headers)
with open('image.png', 'wb') as f:
    f.write(response.content)

#render.json返回请求数据
url = 'http://0.0.0.0:8050/render.json?url=' + target_url + '&wati=5'
response = requests.get(url, headers=headers)
print(response.text)

#execute执行lua脚本
#因为splash支持lua脚本操作
import requests
from urllib.parse import quote

luaScript = '''
function main(splash)
    return 'Python'
end
'''
#lua脚本转码处理
url = 'http://0.0.0.0:8050/execute?lua_source=' + quote(luaScript)
response = requests.get(url)
print(response.text)
