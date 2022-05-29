
# try...except
try:
    a = 10  # int(input("请输入一个整数：\n"))
    b = 20  # int(input("请再输入一个整数：\n"))
    res = a / b
    print("result: ", res)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("输入的不是数字串")


# try...except...else
try:
    n1 = 5  # int(input("输入一个整数：\n"))
    n2 = 0  # int(input("输入一个整数：\n"))
    res = n1 / n2
except BaseException as e:
    print("出错了", e)
else:
    print("result: ", res)


# try...except...else...finally
try:
    n1 = int(input("输入一个整数：\n"))
    n2 = int(input("输入一个整数：\n"))
    res = n1 / n2
except BaseException as e:
    print("出错了", e)
else:
    print("result: ", res)
finally:  # 有无错误都要执行
    print("end")


# 常见的报错
# ZeroDivisionError：除数为0、对0取模
# IndexError：序列中没有这个索引
# KeyError：映射中没有这个键
# NameError：未声明、初始化对象（没有属性）
# SyntaxError：语法错误
# ValueError：传入无效的参数

