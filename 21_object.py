
class Programmer:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

    def __str__(self):
        return "Programmer: name: %s, age: %d" % (self.name, self.age)

pro = Programmer("zz")
print(dir(pro))
print(pro)  # 默认会调用__str__方法

# 特殊属性
print(dir(object))

class A:
    pass

class B:
    pass

class C(A, B):
    def __init__(self, name):
        self.name = name

class D(A):
    pass

x = C("jack")
print(x.__dict__)  # 实例对象的属性值
print(C.__dict__)  # 类的属性值
print(x.__class__)  # 对象所属的类
print(C.__bases__)  # C类父类类型的元素
print(C.__base__)  # 第一个父类
print(C.mro())  # 类的层次结构
print(A.__subclasses__())  # 类的子类


# 特殊方法
a = 15
b = 12
c = a + b
c1 = a.__add__(b)

print(c, c1)

class AA:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):  # 实现了两个对象的相加操作
        return self.name + other.name

    def __len__(self):
        return 100

ss1 = AA("a")
ss2 = AA("b")
print(ss1 + ss2)
print(len(ss1), len(ss2))

print("================================")
# 在对象创建过程中 __new__ 和 __init__ 的作用
class Person:
    def __new__(cls, *args, **kwargs):
        print(f"__new__, cls id = {id(cls)}")
        obj = super().__new__(cls)
        print(f"obj id = {id(obj)}")
        return obj

    def __init__(self, name, age):
        print(f"__init__, self id = {id(self)}")
        self.name = name
        self.age = age


print(f"object class id = {id(object)}")
print(f"Person class id = {id(Person)}")

# 创建对象的过程
p1 = Person("gggg", 18)
print(f"p1 id = {id(p1)}")

# 输出结果
"""
object class id = 140724658739072
Person class id = 1825918976992
__new__, cls id = 1825918976992
obj id = 1825920350768
__init__, self id = 1825920350768
p1 id = 1825920350768
"""

