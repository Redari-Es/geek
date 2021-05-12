import urllib.parse

url = '%2523%25E7%25BC%2596%25E7%25A8%258B%2523'
# 第一次解码
first = urllib.parse.unquote(url)
print(first)
second = urllib.parse.unquote(first)
print(second)
