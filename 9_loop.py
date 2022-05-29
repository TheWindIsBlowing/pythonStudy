
# while 循环
a = 1
while a < 10:
    print(a)
    a += 1

# while循环求1-100中偶数和
sumNum = 0
a = 1
while a <= 100:
    if not a % 2:
        sumNum += a

    a += 1

print(sumNum)

# for-in
for item in "python":
    print(item)

# for range
for i in range(10):
    print(i)

for _ in range(5):
    print("人生苦短，我用python")

# 使用for range打印出 100-1000水仙花数  153 = 1^3 + 5^3 + 3^3
for item in range(100, 1000):
    bai = item // 100
    shi = item % 100 // 10
    ge = item % 10
    print(bai, shi, ge)
    if bai ** 3 + shi ** 3 + ge ** 3 == item:
        print(item)

# else、while 和 for搭配使用
for item in range(3):
    if item > 5:
        print("item > 5")
else:
    print("item < 5")


a = 0
while a < 5:
    if a > 3:
        print("a > 3")

    a += 1
else:
    print("all < 5")

# 双重for循环
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "*", i, "=", i * j, "\t", end="")
    print()
