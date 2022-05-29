
age = 20  # 全局变量

def fun1(a, b):
    c = a + b  # c为局部变量，函数内部可用
    global name
    name = "hello world"
    return c

fun1(10, 50)
print(name, age)
