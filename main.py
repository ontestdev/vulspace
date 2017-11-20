#coding=utf-8
from selenium import webdriver
import time
import xlrd
import sendEmail
import read_data
import naas_account

table = read_data.read_excel_data('E:\\test.xlsx','Sheet1')
for i in range(table.nrows):
    user = table.row_values(i)[0]
    pwd = table.row_values(i)[1]

    naas_account.login(user,pwd)
    content = '用户名：%s 密码：%s' %(user,pwd)
    #sendEmail.send_eamil()
    print(content)


