# encoding:UTF-8

import os
import shutil
import re
import time
import sys

currentPath = ""
path = ""
bk_path = ""


def bye():
    print("\n        Bye!")
    time.sleep(2)
    sys.exit(0)


def delAll(m=0):
    print("是否清空备份文件夹: {} ？(yes / no)".format(bk_path))
    if os.name == 'nt' and m == 0:
        os.system("explorer {}".format(bk_path))
    try:
        s = input("> ")
    except KeyboardInterrupt:
        print("Abort.")
        exit()
    if (s.lower() in ['yes', 'y']):
        for fileList in os.walk(bk_path):
            for name in fileList[2]:
                os.remove(os.path.join(fileList[0], name))
            shutil.rmtree(bk_path)
        if not (os.path.exists(bk_path)):
            print("删除成功！")
    else:
        print("Abort.")
    bye()


def clean(path, bk_path):
    i = 0
    print("Selected path: " + path)
    for dirpath, dirs, files in os.walk(path):
        for dir in dirs:
            if dir.lower() in ['.fseventsd', '.spotlight-v100', '.trashes']:
                i += 1
                filePath = os.path.join(dirpath, dir)
                print("* {} Found... {}".format(i, filePath))
                if (os.path.exists(bk_path + "\\" + dir)):
                    os.rename(bk_path + "\\" + dir,
                              bk_path + "\\" + dir + str(i))
                    shutil.move(filePath, bk_path)
                else:
                    shutil.move(filePath, bk_path)

        for file in files:
            matchObj1 = re.match(r"^\._\S+", file, re.I)
            matchObj2 = re.match(r"\.DS_Store$", file, re.I)

            if matchObj1:
                i += 1
                filePath = os.path.join(dirpath, file)
                print("* {} Found... {}".format(i, filePath))
                if (os.path.exists(bk_path + "\\" + file)):
                    os.rename(bk_path + "\\" + file,
                              bk_path + "\\" + file + str(i))
                    shutil.move(filePath, bk_path)
                else:
                    shutil.move(filePath, bk_path)
            if matchObj2:
                i += 1
                filePath = os.path.join(dirpath, file)
                print("* {} Found... {}".format(i, filePath))
                if (os.path.exists(bk_path + "\\" + file)):
                    os.rename(bk_path + "\\" + file,
                              bk_path + "\\" + file + str(i))
                    shutil.move(filePath, bk_path)
                else:
                    shutil.move(filePath, bk_path)
    if (i == 0):
        print("\n* No trash file found!\n")
        delAll(m=1)
    else:
        delAll()


def mkDir(bk_path):
    if not (os.path.exists(bk_path + "\\MacOS-trash-file-backup")):
        os.mkdir(bk_path + "\\MacOS-trash-file-backup")
    time.sleep(0.5)
    if (os.path.exists(bk_path + "\\MacOS-trash-file-backup")):
        print("备份文件夹创建成功..." + bk_path + "\\MacOS-trash-file-backup")


if __name__ == "__main__":
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    currentPath = os.getcwd()
    print("==============================")
    print("请输入需要处理的目录，例如：C:\ ")
    print("输入 `this` 处理当前目录: {}".format(currentPath))
    try:
        path = input("=> ")
    except KeyboardInterrupt:
        print("Abort.")
        exit()
    print("备份文件夹目录：（不要在处理的目录下！）")
    try:
        bk_path = input("=> ")
    except KeyboardInterrupt:
        print("Abort.")
        exit()
    mkDir(bk_path)
    bk_path = bk_path + "\\MacOS-trash-file-backup"
    if (path.lower() == "this"):
        clean(currentPath, bk_path)
    else:
        path = path + "\\"
        clean(path, bk_path)
