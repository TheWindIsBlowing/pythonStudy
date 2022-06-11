from student import Student

stuInfoFileName = "./studentInfo.txt"
stuTxt = open(stuInfoFileName, "r", encoding="utf-8")
inFileStuInfo = []

for item in stuTxt.readlines():
    inFileStuInfo.append(eval(item))
    if eval(item).get("stuId") > Student.currStuId:
        Student.currStuId = eval(item).get("stuId")
    print(item, end="")
stuTxt.close()
print(f"currStuId: {Student.currStuId}")

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
        return choice, f"你选择了{menuLst[int(choice) - 1]}"
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
        Student.currStuId = Student.currStuId + 1
        stu = Student(Student.currStuId, stuName, englishScore, pythonScore, javaScore)
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
            inFileStuInfo.append(eval(writeInfo))
            print(writeInfo)
            stuInfo.write(writeInfo)
    print(inFileStuInfo)
def checkHaveStu(searchBy, searchVaule):
    res = []
    searchKey = "stuId"
    if(searchBy == 1):
        searchKey = "stuName"
    for item in inFileStuInfo:
        if(item[searchKey] == searchVaule):
            res.append(item)

    return res
def searchInfo():
    while True:
        searchBy = int(input("请选择按学号（0）、或按姓名查询（1）：\n"))
        if(searchBy != 0 and searchBy != 1):
            print("输入有误，请输入0或者1\n")
            continue
        searchValue = ""
        if(searchBy == 0):
            searchValue = int(input("请输入学号：\n"))
        else:
            searchValue = input("请输入姓名：\n")
        res = checkHaveStu(searchBy, searchValue)
        print(res)
        if(len(res) <= 0):
            print(f"没有找到该学生信息，searchBy = {searchBy}，searchValue = {searchValue}\n")
        else:
            print("找到学生信息如下：\n")
            for item in res:
                print(f"stuId:{item.get('stuId')}, stuName:{item.get('stuName')}, englishScore:{item.get('englishScore')}, pythonScore:{item.get('pythonScore')}, javaScore:{item.get('javaScore')}")
        break
def deleteInfo():
    while True:
        showAllInfo()
        delName = input("请输入要删除的姓名（返回上一步请输入0）：\n")
        if(delName == "0"):
            break
        delLst = checkHaveStu(1, delName)
        if(len(delLst) <= 0):
            print(f"没有找到该学生信息：delName = {delName}：")
            continue
        else:
            delNameLst = [item.get('stuName') for item in delLst]
            for item in inFileStuInfo:
                if(item.get('stuName') in delNameLst):
                    inFileStuInfo.remove(item)
                    print("成功删除：", item)
            with open(stuInfoFileName, "w", encoding="utf-8") as stuInfo:
                for item in inFileStuInfo:
                    writeInfo = str(item) + "\n"
                    stuInfo.write(writeInfo)
            break

def modifyInfo():
    while True:
        showAllInfo()
        modifyName= input("请输入要修改的姓名（返回上一步请输入0）：\n")
        if(modifyName == "0"):
            break
        modLst = checkHaveStu(1, modifyName)
        if(len(modLst) <= 0):
            print(f"没有找到该学生信息：modName = {modifyName}")
            continue
        else:
            try:
                stuName = input("请输入学生姓名：\n")
                englishScore = float(input("请输入学生英语成绩：\n"))
                pythonScore = float(input("请输入学生Python成绩：\n"))
                javaScore = float(input("请输入学生java成绩：\n"))
            except:
                print("输入的信息有误，请按照提示重新输入\n")
                continue
            for item in inFileStuInfo:
                if(item.get('stuName') == modifyName):
                    item["stuName"] = stuName
                    item["englishScore"] = englishScore
                    item["pythonScore"] = pythonScore
                    item["javaScore"] = javaScore
            showAllInfo()
            with open(stuInfoFileName, "w", encoding="utf-8") as stuInfo:
                for item in inFileStuInfo:
                    writeInfo = str(item) + "\n"
                    stuInfo.write(writeInfo)
            break
def sortInfo():
    while True:
        sortChoice = int(input("请选择按升序（0）、或降序（1）排序：\n"))
        if(sortChoice != 0 and sortChoice != 1):
            print("输入有误，请输入0或者1\n")
            continue
        sortMode = int(input("请选择排序方式（0.按总成绩排序，1.按英语成绩排序，2.按python成绩排序，3.按java成绩排序）：\n"))
        if(sortMode not in [i for i in range(0, 4)]):
            print("请输入0-3的整数\n")
            continue

        corseName = ["englishScore", "pythonScore", "javaScore"]
        if(sortMode in [i for i in range(1, 4)]):
            inFileStuInfo.sort(key=lambda x: int(x[corseName[sortMode - 1]]),
                               reverse=True if sortChoice == 0 else False)
        elif(sortMode == 0):
            inFileStuInfo.sort(key=lambda x: int(x[corseName[0]]) + int(x[corseName[1]]) + int(x[corseName[2]]),
                               reverse=True if sortChoice == 0 else False)

        showAllInfo()
        with open(stuInfoFileName, "w", encoding="utf-8") as stuInfo:
            for item in inFileStuInfo:
                writeInfo = str(item) + "\n"
                stuInfo.write(writeInfo)
        break

def countInfo():
    print(f"所有学生人数： {len(inFileStuInfo)}")
def showAllInfo():
    print("所有学生信息：")
    for item in inFileStuInfo:
        print(item)

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