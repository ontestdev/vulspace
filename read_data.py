#coding=utf-8
'''
data = open('data.txt','r')
lines = data.readlines()
for line in lines:
    key = line.split('=')[0]
    val = line.split('=')[1]
    print(val)
'''
import xlrd
def read_excel_data(file,name):
    data = xlrd.open_workbook(file)
    table = data.sheet_by_name(name)
    return table



