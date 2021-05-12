import time
import requests_cache


def make_throttle_hook(delay=1.0):
    def hooks(response, *args, **kwargs):
        #如果没有缓存，则添加延时
        if not getattr(response, 'from_cache', False):
            print('delayTime')
            time.sleep(delay)
            return response

        return hooks


if __name__ == "__main__":
    requests_cache.install_cache()
    requests_cache.clear()
    #钩子函数的使用
    s = requests_cache.CachedSession()
    s.hooks = {'response': make_throttle_hook(2)}
    s.get('http://127.0.0.1:5000/')
    s.get('http://127.0.0.1:5000/')

#设置不同的存储机制
#import requests_cache
#设置memory存储
#requests_cache.install_cache(backend='memory')
#设置sqlite存储
#requests_cache.install_cache(backend='sqlite')
#设置redis存储
#requests_cache.install_cache(backend='redis')
#设置mongo存储
#requests_cache.install_cache(backend='mongo')
