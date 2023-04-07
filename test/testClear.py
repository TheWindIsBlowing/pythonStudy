# coding=utf-8

import shutil
import os

clearDir = r"C:\Users\YGamer\Desktop\原特效资源"

if __name__ == "__main__":
    print("hello testClear")

    for root, dirs, files in os.walk(clearDir):
        for file in files:
            path = os.path.join(root, file)
            # print(path)
            if os.path.splitext(path)[-1] == ".meta":
                print(path)
                os.remove(path)

    