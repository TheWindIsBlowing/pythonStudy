
def add(a, b):
    print("a: %d, b: %d" % (a, b))
    return a + b


print(add(20, 5))  # 位置传参
print(add(b=30, a=12))  # 关键字传参，根据形参名字传递参数

"""
在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值，arg1修改后，n1还是原来的值
如果是可变对象，在函数体的修改会影响到实参的值，arg2修改后，n2中append了一个10，变成[23, 30, 10]了
"""
def fun(arg1, arg2):
    print("start arg1: {0}, arg2: {1}".format(arg1, arg2))
    arg1 = 100
    arg2.append(10)
    print("end arg1: {0}, arg2: {1}".format(arg1, arg2))


n1, n2 = 95, [23, 30]
print("start1 n1: {0}, n2: {1}".format(n1, n2))
fun(n1, n2)
print("end1 n1: {0}, n2: {1}".format(n1, n2))


# 函数返回值
# 1.如果函数没有返回值，return可省略不写
# 2.函数返回值为1个，直接返回那个类型的值
# 3.函数返回值有多个，返回的结果为一个元组
def oddOrEven(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)

    return odd, even


lst = [10, 29, 34, 23, 44, 53, 55]
print(oddOrEven(lst))

# 默认值参数
def fun1(a, b = 23):
    print(f"a: {a}, b: {b}")

fun1(1)
fun1(1, 2)

# 函数定义时，个数可变的 位置形参（positional arguments）
def fun2(*args):  # 可以传递任意个参数  args为一个元组
    print(args)

fun2(10)
fun2(10, 20)
fun2(10, 15, 30)

# 个数可变的 关键字形参（keyword-only argument）
def fun3(**kwargs):  # kwargs为一个字典
    print(kwargs)

fun3(a = 10)
fun3(name = 10, age = 1)
fun3(sex = 10, a = 20, c = 15)

# 在函数定义时，既有个数可变的关键字形参，也有个数可变的位置形参时
# 个数可变的位置形参需要放在前面
def fun4(*args, **kwargs):
    pass

def fun5(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")

fun5(*[10, 20, 30])  # 将列表中每个元素转换成位置实参传入
fun5(**{"b": 10, "a": 20, "c": 30})  # 将字典中每个键值对转换成关键字实参传入

def fun6(a, b, *, c, d):  # * 之后的形参只能使用关键字形参
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")

fun6(10, 20, c = 30, d = 40)




