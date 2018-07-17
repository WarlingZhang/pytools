#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 批量重命名

import os
import sys


# 重命名
# os.rename("test","test2")

# print "重命名成功。"

# 列出重命名后的目录
# print "目录为: %s" %os.listdir(os.getcwd())


def rename_files(filelist, old, new):
    for f in filelist:
        print(f)
        # if "aa.txt" in f:
        new_name = ''
        if '^' == old:
            new_name = new + f
        elif '$' == old:
            new_name = f + new
        else:
            new_name = f.replace(old, new)
        os.rename(f, new_name)
        print(f, "重命名为", new_name)


if __name__ == '__main__':
    # 用法 python3 batch_rename.py E:\works\doc\船舶\kettle_local "^" local
    argv = sys.argv
    print(argv)
    path = argv[1]
    # path = ".\\"
    print("当前路径", os.getcwd())


    # 列出目录
    # dirs = os.listdir(os.getcwd())
    os.chdir(path)
    files = os.listdir(path)
    print("当前路径", os.getcwd())
    # print("文件列表为: ", files)
    rename_files(files, argv[2], argv[3])
