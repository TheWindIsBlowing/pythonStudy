
# 变量的赋值操作
# 只是形成了两个变量，实际上还是指向同一个对象
class Cpu:
    pass
class Disk:
    pass
class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = Cpu()
cpu2 = cpu1
print(id(cpu1), cpu1)
print(id(cpu2), cpu2)

disk = Disk()
com = Computer(cpu1, disk)

# 类的浅拷贝
# python中拷贝一般都是指的浅拷贝，拷贝时对象包含的子对象内容不拷贝
# 因此，源对象与拷贝对象会引用同一个子对象
import copy
com2 = copy.copy(com)
print(com, com.cpu, com.disk)
print(com2, com2.cpu, com2.disk)

# 深拷贝
# 使用copy模块中的deepcopy函数，递归拷贝对象中包含的子对象
# 源对象和拷贝对象所有的子对象也不相同
com3 = copy.deepcopy(com)
print(com3, com3.cpu, com3.disk)
