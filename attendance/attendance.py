import math
import xlrd
import xlwt
from datetime import date,datetime

work_on_time = '08:40'
work_off_time = '17:30'


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\zwl\Desktop\临时表\2017-10打卡.xls')
    # 获取所有sheet
    # print(workbook.sheet_names()) # [u'sheet1', u'sheet2']
    # sheet2_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0) # sheet索引从0开始
    # sheet2 = workbook.sheet_by_name('sheet2')

    # sheet的名称，行数，列数
    # print(sheet.name,sheet.nrows,sheet.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet.row_values(3) # 获取第四行内容
    cols = sheet.col_values(2) # 获取第三列内容
    date_set = set()
    date_dict = {}

    for i in range(1, len(cols)):
        name:str = cols[i]
        if name is None:
            continue
        name = name.strip()
        if name == '张文良':
            date = sheet.cell_value(i,3)
            time = sheet.cell_value(i,4)
            vals = date_dict.get(date)
            if vals is None:
                vals = []
                date_dict[date]=vals
            vals.append(time)
            date_set.add(date)

    # print(rows)
    # print(cols)
    # print(date_set)
    l = list(date_set)
    l.sort()
    # print(l)
    # print(date_dict)

    for d in l:
        time: list = date_dict.get(d)
        time.sort()
        begin = time[0]
        end = time[-1]
        if begin>work_on_time or end < work_off_time:
            print('迟到或早退')
            print('--------------begin--------------')
            print(d)
            print(begin, end)
            print('--------------end--------------')
        # elif end < work_off_time

    # 获取单元格内容
    # print(sheet.cell(1,0).value.encode('utf-8'))
    # print(sheet.cell_value(1,0).encode('utf-8'))
    # print(sheet.row(1)[0].value.encode('utf-8'))

    # 获取单元格内容的数据类型
    # print(sheet.cell(1,0).ctype)


if __name__ == '__main__':
    # read_excel()
    t1 = datetime.strptime('09:52', "%H:%M")
    t2 = datetime.strptime('17:43', "%H:%M")
    delta = t2 - t1
    offset_min = math.floor(delta.seconds/60)
    print(delta.days)
    print(delta.total_seconds())
    print(delta.seconds)
    print(offset_min)
    print(1,2)