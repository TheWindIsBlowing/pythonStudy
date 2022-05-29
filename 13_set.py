
# 集合的创建
s = {3, 6, 5, 1}
print(s)
s0 = set({1, 2, 3, 3, 2, 1})
print(type(s0), s0)

s1 = set(range(1, 11, 2))
print(type(s1), s1)
s2 = set([1, 1, 3, 5, 5])
print(type(s2), s2)
s3 = set((10, 10, 11, 5, 9))
print(type(s3), s3)
s4 = set("python")
print(type(s4), s4)

# 空集合
s5 = set()
print(type(s5), s5)

# in、not in、add、update
s6 = {10, 9}
print(10 in s6)
print(10 not in s6)
print(s6)
s6.add(100)
print(s6)
s6.update({10, -10})
print(s6)

# remove、discard、pop、clear

# issubset、issuperset、isdisjoint

# 集合的数学操作
# 1.交集
s5.intersection(s6)
s5 & s6
# 2.并集
s6.union(s5)
s5 | s6
# 3.差集
s5 - s6
s5.difference(s6)
# 4.对称差集
s6.symmetric_difference(s5)
s5 ^ s6

# 集合生成式
s8 = {i * 2 for i in range(10)}
