
from decimal import Decimal

# 整型
num = 123
print(id(num)) # 变量内存地址
print(type(num)) # 变量类型
print(num)

# 浮点数
n1 = 1.1
n2 = 2.2
n3 = 2.1

print(n1 + n2) # 精度有问题
print(Decimal("1.1") + Decimal("1.2")) # 使用decimal库解决这个问题
print(n1 + n3)

# bool
f1 = True
f2 = False
print(f1 + 1)
print(f2 + 1)

# 字符串
str1 = '人生苦短，' \
       '我用python'
str2 = "人生苦短，我用python"
str3 = '''人生苦短，
        我用python'''
str4 = """人生苦短，
        我用python"""
print(str1)
print(str2)
print(str3)
print(str4)

# 类型转换 str() 、 int() 、 float


name = "张三"
age = 18
print("我叫" + name + "今年" + str(age))
