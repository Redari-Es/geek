# TODO: 截取  <13-05-21, Redari-Es> #
#字符串截取
str = 'ABCDEFG'
#截取第一位到第三位的字符
print('截取第一位到第三位的字符:' + str[0:3:])
#截取字符串的全部字符
print('截取字符串的全部字符:' + str[::])
#截取第七个字符到结尾
print('截取第七个字符到结尾:' + str[6::])
#截取从头开始到倒数第三个字符之前
print('截取从头开始到倒数第三个字符之前:' + str[:-3:])
#截取第三个字符
print('截取第三个字符:' + str[2])
#截取倒数第一个字符
print('截取倒数第一个字符:' + str[-1])
#与原字符串顺序相反的字符串
print('与原字符串顺序相反的字符串:' + str[::-1])
#截取倒数第三位与倒数第一位之前的字符
print('截取倒数第三位与倒数第一位之前的字符:' + str[-3:-1:])
#截取倒数第三位到结尾
print('截取倒数第三位到结尾:' + str[-3::])
#逆序截取
print('逆序截取：' + str[:-5:-3])