
# ==, is, is not
a = 20
b = 20

print(id(a), id(b))
print(a == b)
print(a is b)

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1), id(list2))
print(list1 == list2)
print(list1 is not list2)

# and, or, not
aa, bb = 10, 20
print(not aa)

# in, not in
str1 = "hello"
print("w" in str1)
print("i" not in str1)
