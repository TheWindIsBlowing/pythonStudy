
# python中一切皆对象
# 测试对象的布尔值  一下对象布尔值全为False
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(""))
print(bool([])) # 空列表
print(bool(list())) # 空列表
print(bool(())) # 空元组
print(bool(tuple())) # 空元组
print(bool({})) # 空字典
print(bool(dict())) # 空字典
print(bool(set())) # 空集合

# 其余对象是True

# if
money = 1000
s = 20 # int(input("请输入取款金额\n"))
if money >= s:
    money -= s
    print("取款成功，余额为" + str(money))

# if...else
num = 5 # int(input("请输入一个整数\n"))
if num % 2 == 0:
    print(str(num) + "是偶数")
else:
    print(str(num) + "是奇数")

# if...elif...elif...else
score = 99 # int(input("请输入一个分数\n"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 50 <= score < 60:
    print("E")
else:
    print("分数有误")

# 条件表达式  类比其他语言的三目运算符 ？ ：
num1, num2 = 25, 30
print("num1 > num2" if num1 > num2 else "num1 <= num2")

# pass 语句使用
if True:
    pass # 程序运行时不报错，啥都不做
else:
    print("ha")

# range() 内置函数
r = range(10) # 默认从0开始，步长为1
print(r) # range(0, 10)
print(list(r)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(1, 10) # 步长为1
print(r) # range(1, 10)
print(list(r)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(1, 10, 2) # 从1开始到10结束（不包含10），步长为2
print(r) # range(1, 10， 2)
print(list(r)) # [1, 3, 5, 7, 9]

# 判断指定整数是否在序列中
print(10 in r)
print(10 not in r)

