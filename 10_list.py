
a = 10  # 变量存储的是一个对象的引用
list1 = ["hello", "python", 98, 1.5]
list2 = list([])
print(id(list1))
print(type(list1))
print(list1)
print(list2)

# 从前往后索引为 0 - (len - 1)
# 从后往前索引为 -1 - (-len)
print(list1[0], list1[-len(list1)])
print(list1.index(98))
print(list1.index(98, 1, 3))

# 切片
list3 = [10, 20, 30, "liu", "fu"]
list4 = list3[1:4:2]  # start 1, end 4, step 2
print(id(list3), list3)
print(id(list4), list4)

# 步长为负数的情况
print(list3[::-1])  # 相当于把list3逆序


# 列表添加元素 append、extend、insert
lst = [10, 20, 30, "a", "b", "c"]
lst2 = ["liu", "feng", "hong"]
print("lst原始列表：", lst)
lst.append(100)
print(lst)
lst.extend(lst2)
print(lst)
lst.insert(1, 10000)
print(lst)

# 列表删除元素 remove...

# 列表排序 sorted()  sort

# 列表生成式
ls = [i for i in range(1, 9)]
ls2 = [i ** 2 for i in range(1, 9)]
print(ls)
print(ls2)

