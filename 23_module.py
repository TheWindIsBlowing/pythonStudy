
# 一个python脚本文件就是一个模块
# 一个模块可以包含：函数、类、语句...
# 类可以包含：类属性、类方法、静态方法...
def func1():
    pass

def func2():
    pass

class Student:
    nativePlace = "cn"

    def __init__(self, name):
        self.name = name

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass


import math  # 导入整个模块
print(id(math))
print(type(math))
print(math)
print(math.pi)
print("-========================-")
print(dir(math))
print(math.pow(2, 8))

from math import pi  # 导入模块中的  函数、变量、类
print(pi)


# 导入自定义的模块
# improt 23_module2  模块名不符合规范
import calc  # 这里并没有运行calc中 以主程序方式运行的代码
print(calc.add(10, 200))
