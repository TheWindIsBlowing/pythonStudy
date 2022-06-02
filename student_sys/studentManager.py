import os.path
import student

stuInfoFileName = "./studentInfo.txt"
stuTxt = open(stuInfoFileName, "r", encoding="utf-8")
inFileStuInfo = []
currStuId = -1
for item in stuTxt.readlines():
    inFileStuInfo.append(item)
    if eval(item).get("stuId") > currStuId:
        currStuId = eval(item).get("stuId")
    print(item, end="")
stuTxt.close()
print(f"currStuId: {currStuId}")

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
    stuLst = []
    while True:
        try:
            stuName = input("请输入学生姓名：\n")
            englishScore = float(input("请输入学生英语成绩：\n"))
            pythonScore = float(input("请输入学生Python成绩：\n"))
            javaScore = float(input("请输入学生java成绩：\n"))
        except:
            print("输入的信息有误，请按照提示重新输入\n")
            continue
        stu = student.Student(++currStuId, stuName, englishScore, pythonScore, javaScore)
        stuLst.append(stu.showInfo())

        isEnd = False
        while True:
            continueInsert = input("继续插入学生信息吗？（Y / N）：")
            if continueInsert == "Y" or continueInsert == "y":
                break
            elif continueInsert == "N" or continueInsert == "n":
                isEnd = True
                break
            else:
                print("输入有误，请输入（Y / N）：")
                continue

        if isEnd:
            saveInfo(stuLst)
            break

def saveInfo(stuLst):
    print(f"你一共插入了{len(stuLst)}条学生信息：\n")
    with open(stuInfoFileName, "a", encoding="utf-8") as stuInfo:
        for item in stuLst:
            writeInfo = str(item) + "\n"
            print(writeInfo)
            stuInfo.write(writeInfo)

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