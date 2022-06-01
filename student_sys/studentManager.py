menuLst = ["退出系统啊啊",
           "录入学生信息",
           "查找学生信息",
           "删除学生信息",
           "修改学生信息",
           "排序学生信息",
           "统计学生人数",
           "显示所有学生"];


def showMenu():
    print("===============================学生管理系统================================")
    print("==                              功能菜单                                ==")
    for i in range(1, len(menuLst) + 1):
        print(f"==                           {str(i)}.{menuLst[i - 1]}                              ==")
    print("=================================end=====================================")


def getChoiceMenu():
    choice = input("请输入想要使用的功能（1-8）：\n")
    if choice in [str(i) for i in range(1, len(menuLst) + 1)]:
        return choice, f"你选择了{menuLst[int(choice) - 1]}\n"
    else:
        return "0", "输入错误，请输入1-8的数字：\n"

def insertInfo():
    pass
def searchInfo():
    pass
def deleteInfo():
    pass
def modifyInfo():
    pass
def sortInfo():
    pass
def countInfo():
    pass
def showAllInfo():
    pass

if __name__ == "__main__":
    while True:
        showMenu()
        choiceTuple = getChoiceMenu()
        print(choiceTuple[1])
        if choiceTuple[0] == "0":
            continue
        elif choiceTuple[0] == "1":
            break
        elif choiceTuple[0] == "2":
            insertInfo()
        elif choiceTuple[0] == "3":
            searchInfo()
        elif choiceTuple[0] == "4":
            deleteInfo()
        elif choiceTuple[0] == "5":
            modifyInfo()
        elif choiceTuple[0] == "6":
            sortInfo()
        elif choiceTuple[0] == "7":
            countInfo()
        elif choiceTuple[0] == "8":
            showAllInfo()