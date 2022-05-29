
# 字典创建方式
dic1 = {"张三": 85, "李四": 70, "王五": 50}
print(id(dic1), type(dic1), dic1)

dic2 = dict(name="hack", age=18)
print(id(dic2), type(dic2), dic2)

# 获取字典中元素
print(dic1["张三"])  # 查找不到时会报错

print(dic2.get("name"))
print(dic2.get("sex"))  # 查找不到时返回None
print(dic2.get("sex", "男"))  # 没找到时返回默认值

del dic1["张三"]
dic1["陈六"] = 100
print(dic1)

# 视图操作  获取所有key,value, kye-value对
keys = dic1.keys()
valus = dic1.values()
print(type(keys), keys, type(valus), valus)
print(list(keys))  # 将所有key组成的视图转换成列表
print(list(valus))
print(dic1.items())
print(list(dic1.items()))  # 元组

# 字典的遍历
for item in dic1:
    print(item, dic1[item], dic1.get(item))

# 字典生成式
items = ["Fruits", "Books", "Others"]
prices = [96, 50, 23]
# items和prices长度不相同时，zip只会有短的个数
d = {item: price for item, price in zip(items, prices)}
print(d)
