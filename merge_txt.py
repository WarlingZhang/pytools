#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 把多个文本文件合并成一个 生成的文件名，通过命令行传入，如果不传，默认merge.txt
import codecs
import os

import sys

# encoding = "utf-8"
encoding = "gbk"


def copy_files(srcfile, targetfile):
    # targetfile.write("\n--"+srcfile+"\n")
    targetfile.write("\n\n")
    with codecs.open(srcfile, encoding=encoding) as f:
        for line in f:
            targetfile.write(line)
            # print(line)


if __name__ == '__main__':
    # 使用方法: python merge_txt.py D:\works\temp final.sql
    #                              文件坐在目录    要生成的文件名称
    path = ""
    targetfile = "merge.txt"
    if len(sys.argv) >= 3:
        path = sys.argv[1]
        targetfile = sys.argv[2]
    elif len(sys.argv) == 2:
        targetfile = sys.argv[1]

    # path = ".\\"
    print("当前路径", os.getcwd())

    # 列出目录
    # dirs = os.listdir(os.getcwd())
    os.chdir(path)
    files = os.listdir(path)
    print("当前路径", os.getcwd())
    # print("文件列表为: ", files)
    with codecs.open(targetfile, 'w', encoding) as o:
        for f in files:
            copy_files(f, o)

