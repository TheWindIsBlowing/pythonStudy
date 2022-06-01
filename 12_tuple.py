
# 可变序列 修改后内存地址不变
# 列表、字典
lst = [10, 20, 30]
print(id(lst))
lst.append(10000)
print(id(lst))

# 不可变序列 修改后内存地址改变
# 字符串、元组
s = "hello"
print(id(s))
s += "world"
print(id(s))

# 创建元组
t = ("python", "golang", 100)
print(type(t))
print(t)

t2 = "hah", "gg", 45, False  # 省略小括号
print(type(t2))
print(t2)

t1 = tuple(("java", "world", 200))
print(type(t1))
print(t1)

# 注意，如果元组中只有一个元素，需要加上一个逗号
t3 = "tt",  # t3 = ("tt",)
print(type(t3))
print(t3)


# 类比一下列表、字典空对象的创建
lst = []
lst1 = list()

dic = {}
dic1 = dict()

tup = ()
tup1 = tuple()
print(lst, lst1)
print(dic, dic1)
print(tup, tup1)

# 元组遍历
tupTemp = (10, 20, [50, "gg"], False, {})
for item in tupTemp:
    print(item)

print(tupTemp[0])
