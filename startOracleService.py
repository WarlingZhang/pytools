# OracleOraDb11g_home1TNSListener
# OracleServiceORCLGBK

import os

lines = os.popen("sc query OracleOraDb11g_home1TNSListener |findstr RUNNING").readlines()
resultLen = len(lines)
if resultLen == 1:
    print("正在运行")
else:
    print("你找的服务已死，有事请烧纸")
