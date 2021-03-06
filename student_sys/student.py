
# 学生模块
class Student:
    currStuId = -1

    def __init__(self, stuId, stuName, enScore, pyScore, jaScore):
        self.stuId = stuId
        self.stuName = stuName
        self.englishScore = enScore
        self.pythonScore = pyScore
        self.javaScore = jaScore
        self.totalScore = enScore + pyScore + jaScore

    def showInfo(self):
        print(f"{self.stuId}\t{self.stuName}\t{self.englishScore}\t{self.pythonScore}\t{self.javaScore}\t{self.totalScore}")
        return {"stuId": self.stuId,
                "stuName": self.stuName,
                "englishScore": self.englishScore,
                "pythonScore": self.pythonScore,
                "javaScore": self.javaScore}
