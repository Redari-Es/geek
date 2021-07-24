# TODO: 查找find/index  <13-05-21, Redari-Es> #
str = 'ABCDABC'
#查找全部
print(str.find('A'))
print(str.index('A'))
#输出内容
#从字符串第4个开始查找
print(str.find('A', 3))
print(str.index('A', 3))
#从字符串第2个到第6个开始查找，
print(str.find('C', 1, 5))
print(str.index('C', 1, 5))
#查找不存在的内容
print(str.find('E'))
print(str.index('E'))
