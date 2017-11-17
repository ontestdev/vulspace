#coding=utf-8
from selenium import webdriver
import time
import xlrd
import send_eamil
import read_data


def account_login():
    bro = webdriver.Firefox()
    bro.get('http://192.168.211.99/naas/account/login.html')
    user_ele = bro.find_element_by_class_name('form-control')
    password_ele = bro.find_element_by_css_selector('input[type="password"]')
    user_ele.send_keys(list[0])
    password_ele.send_keys(list[1])
    time.sleep(1)
    btn = bro.find_element_by_class_name('btn-login').click()
    try:
        bro.find_element_by_class_name('loginTips')
        error_msg = '登录有异常！'
        contant = '用户名：%s  密码：%s'%(list[0],list[1])
        send_eamil.send_eamil('测试测试，纯属测试'+ '\n' + contant + '\n' + error_msg)
    except:
        print('ok')
    time.sleep(2)
    bro.close()



if __name__ == '__main__':

    table = read_data.read_excel_data('e:\\test.xlsx',u'Sheet1')
    for i in range(table.nrows):
        list = table.row_values(i)
        account_login()
        contant = '用户名：%s  密码：%s'%(list[0],list[1])
        print(contant)
        print('*'*20)













