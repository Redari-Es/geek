import re
#匹配字符串中所有含有'oo'字符的单词
#当re中没有圆括号时，列表中的字符串表示整个re匹配的内容
find_value = re.findall('\w*oo\w*', "woo this foo is too")
print(find_value)
#获取字符串中所有的数字字符串
#当re中只带有一个圆括号时，列表中的元素为字符串
#并且该字符串的内容与括号中的re相对应
find_value = re.findall('.*?(\d+).*?', 'adsd12343.j134d5645fd789')
print(find_value)
add = 'https://www.net.com.edu//action=?asdfsd and other https://www.baidu.com//a=b'
find_value = re.findall('((w{3}\.)(\w+\.)+(com|edu|cn|net))', add)
print(find_value)
