
a = 'python'
b = "python"
c = """python"""
print(id(a), a)
print(id(b), b)
print(id(c), c)

# 查找
s1 = "hellO,Python"
print(s1.index("l"))
print(s1.rindex("l"))
print(s1.find("l"))
print(s1.rfind("l"))

# 大小写
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.capitalize())
print(s1.title())

# 内容对齐
print(s1.center(20, "*"))
print(s1.ljust(20, "*"))
print(s1.rjust(20, "*"))
print(s1.zfill(20))  # 右对齐，使用0填充

# 分割
print(s1.split(","))
print(s1.split(sep=","))
print(s1.split(sep=",", maxsplit=1))

s2 = "g|gg|jkj|"
print(s2.rsplit(sep="|", maxsplit=2))

# 判断
print(s2.isidentifier())  # 由字母、数字、下划线组成的字符串是合法的标识符
print("_".isidentifier())
print("\t\n".isspace())  # 字符串是否由（空格、回车、换行、水平制表符）组成
print("haha张".isalpha())

# 替换
print("hello python".replace("l", "L", 1))
print("_".join(["name", "haha", "ga"]))
print("_".join("python"))

# 比较
print("apple" > "dog")
print(ord("a"))
print(chr(97))

# 切片
print("hello python"[:2])
print("hello python"[::2])
print("hello python"[::-1])

# 格式化
# % 元组
print("my name is %s, %d years old." % ("zhangsan", 18))
# format
print("my name is {0}, {1} years old.".format("zhangsan", 18))
# f-string
name1 = "zhangsan"
age = 18
print(f"my name is {name1}, {age} years old.")

print("%10d" % 50)  # 宽度
print("%.3f" % 3.1415926)  # 保留三位小数
print("%10.3f" % 3.1415926)  # 宽度10且保留三位小数

print("{0:.3}".format(3.1435926))  # 一共三位数
print("{0:.3f}".format(3.1435926))  # 保留三位小数
print("{0:10.3f}".format(3.1435926))  # 宽度10且保留三位小数

# 编码
gbkE = "猪牛".encode(encoding="GBK")
utf_8 = "猪牛".encode(encoding="UTF-8")
print(gbkE)  # 在GBK编码格式中，一个中文占两个字节
print(utf_8)  # 在UTF-8编码格式中，一个中文占三个字节
# 解码
print(gbkE.decode(encoding="GBK"))
print(utf_8.decode(encoding="UTF-8"))