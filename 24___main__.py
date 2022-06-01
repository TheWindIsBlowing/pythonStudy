import os


def print_hi(name):
    print(f'Hi, {name}')

# 以主程序方式运行，其他模块导入此模块时，if中代码不会运行
if __name__ == '__main__':
    print_hi('PyCharm')

    for p in os.listdir("./dir"):
        file = os.path.join("./dir", p)
        if os.path.isfile(file):
            os.remove(file)