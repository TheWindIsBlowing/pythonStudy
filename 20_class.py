class Student:
    # 类属性
    studentName = "zhangsan"
    nativeAddr = "cn"

    # 初始化方法
    def __init__(self, name, addr, nick):
        self.name = name  # self.name 实例属性
        self.addr = addr
        self.__nick = nick  # 双下划线表示该变量 外部不能直接通过.__nick访问

    # 实例方法
    def eat(self):
        print(self, "eat")

    # 静态方法
    @staticmethod
    def fun1():
        print("我是Student的静态方法")

    # 类方法
    @classmethod
    def fun2(cls):
        print("我是Student的类方法")


print(id(Student), "\n", type(Student), "\n", Student)
student1 = Student("a", "cn_hk", "fat man")
print(id(student1), "\n", type(student1), "\n", student1)
student1.eat()
print(student1.name)
print(student1.addr)
print(student1.studentName)
print(student1.nativeAddr)

Student.eat(student1)  # student1.eat() 功能相同

# 类属性的使用 实例共享

# 为类实例动态绑定属性和方法
student1.gender = "男"
print(student1.gender)


def show():
    print("show  ggg")


student1.show = show
student1.show()
print(dir(student1))
print(student1._Student__nick)


# 面向对象三大特征：封装、继承、多态


# 继承
# 如果一个类没有继承任何类，则默认继承object
# 支持多继承
# 定义子类时，必须在其构造函数中调用父类的构造函数
class Person(object):  # Person继承object  可省略
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"姓名：{self.name}, 年龄：{self.age}")

class Programmer(Person):  # Programmer继承Person
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

class Teacher(Person):
    def __init__(self, name, age, teacherYears):  # 重写__init__方法
        super().__init__(name, age)
        self.teacherYears = teacherYears
    def fun(self):
        print("teacher")

pro = Programmer("liu", 18, 99)
pro.info()

tea = Teacher("gg", 18, 10)
tea.fun()
tea.info()

# 具备多态特性
class Animal:
    def eat(self):
        print("animal eat")

class Cat(Animal):
    def eat(self):
        print("cat eat")

class Dog(Animal):
    def eat(self):
        print("dog eat")


# python 是动态语言，monster只要有eat方法，那么通过调用func也可以调用到Monster的eat方法
class Monster:
    def eat(self):
        print("monster eat")

def func(animal):
    animal.eat()

func(Dog())
func(Cat())
func(Monster())

print(Student.nativeAddr)