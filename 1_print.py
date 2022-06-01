# coding=utf-8
'''
通常，在python 文件，尤其是包含中文的python文件中，需要说明你的Python源程序文件使用的编码；
如果未声明，程序默认使用ascii码来写，此时，书写中文的话python解释器一般会报错。
pyCharm python文件默认编码为utf-8

常见的编码声明：
# coding=utf-8
# coding:utf-8
# -*-coding=utf-8-*-
# -*-coding:utf-8-*-
注意：
①coding后面使用:或=都可以。
②:或=与coding之间不能有空格，而:或=与编码之间有没有空格均可。
③编码声明一般放在python文件开头（第一行或第二行）
'''

# print()
# 输出到标准输出流
print(555)
print(98.5)

print('python')
print("python")

# 输出到文件中
fp = open("1_print_test.txt", "w")
print("i love pytho", file=fp)
fp.close()

# 不换行
print("hello", "world", "!")

# 转义字符
print("hello    python")
print("hello\npython") # \n 换行
print("hello\tpython") # \t 制表符
print("hello\rpython") # \r 回车
print("hello\bpython") # \b 退格

# 原字符 不希望字符串中的转义字符起作用
# 字符串之前加上 r 或者 R
print(r"hello\tpython")
# 注意 这种情况下最后一个字符不能是反斜杠
# print(r"hello python\")

