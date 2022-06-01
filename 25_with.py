
"""
一个类同时实现了__enter__和__exit__方法时，称该类遵守了上下文管理器协议
该类的实例对象称为上下文管理器
"""
class MyContentMgr:
    def __enter__(self):
        print("MyContentMgr enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("MyContentMgr exit")

    def show(self):
        print("MyContent show")

print(type(MyContentMgr()))
print(open("./25_with.txt", "w"))

with MyContentMgr() as content:  # 相当于content = MyContentMgr
    content.show()

# with open("./25_with.txt", "w") as file:
#     print()

