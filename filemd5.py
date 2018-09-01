
import hashlib
import os
import datetime
import sys


def getfilemd5(filename):
    """
    计算文件的md5值
    :param filename: 需要计算md5的文件名，包含路径
    :return:
    """
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

# filepath = raw_input('请输入文件路径：')
# filepath = "D:\\Users\\warling\\Downloads\\mysql-installer-community-5.7.23.0.msi"
argv = sys.argv
filepath = argv[1]
# 输出文件的md5值以及记录运行时间
starttime = datetime.datetime.now()
md5 = getfilemd5(filepath)
print("md5值：", md5)
endtime = datetime.datetime.now()
print('运行时间：%ds' % (endtime-starttime).seconds)

