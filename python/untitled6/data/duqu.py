#！/user/bin/python
#-*- coding:utf-8 -*-
import xlrd
def shuju():
    num_1=[]
    f=xlrd.open_workbook(r'F:\学习总结\python\untitled6\data\bieke_test.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        num_1.append(sheet.row_values(i))
    return num_1
if __name__=="__main__":
    print(shuju())