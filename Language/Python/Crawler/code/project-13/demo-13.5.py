# TODO: 尝试数据清洗  <13-05-21, Redari-Es> #
import requests


def city_name():
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Referer': 'https://kyfw.12306.cn/otn/login/init'
    }
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9031'
    city_code = requests.get(url, headers=headers, verify=False)
    #数据使用字符串操作处理
    city_code_list = city_code.text.split("|")
    city_dict = {}
    for k, i in enumerate(city_code_list):
        if '@' in i:
            #城市名作为字典的键，城市编号作为字典的值
            city_dict[city_code_list[k + 1]] = city_code_list[k + 2].replace(
                ' ', '')
    return (city_dict)


#输出
print(city_name())
