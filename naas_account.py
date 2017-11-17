#coding = utf-8
from selenium import webdriver
import time
#import HTMLTestRunner

#import pytest
'''
模块主要划分为
openBrowers
loadUrl
find_element
send_values
check_result

'''
bro = webdriver.Firefox()
bro.get('http://192.168.211.99/naas/account/')

def login():

    print (bro.title)
    user_ele = bro.find_element_by_class_name('form-control')
    password_ele = bro.find_element_by_css_selector('input[type="password"]')
    time.sleep(1)
    user_ele.send_keys('zhouss')
    time.sleep(1)
    password_ele.send_keys('zhouss123')
    time.sleep(1)
    btn = bro.find_element_by_class_name('btn-login').click()
    bro.maximize_window()
    time.sleep(1)
    print(bro.get_cookies())
    print(bro.get_cookie('sessionid'))
    bro.add_cookie({'name':'ssss','value':'hahahah'})
    print(bro.get_cookies())
    bro.delete_cookie('ssss')
    print(bro.get_cookies())

def dis_customer():
    #分销客户
    bro.find_element_by_xpath('//*[@id="index"]/div[2]/ul/li[4]/ul/li[1]/a').click()
    time.sleep(5)
    try:
        #操作按钮
        opera = bro.find_element_by_xpath('//*[@id="disCustomer"]/div[2]/table/tbody/tr[2]/td[8]/div/button')
        opera.click()
    except:
        print("操作失败")
    #折扣按钮
    bro.find_element_by_xpath('//*[@id="disCustomer"]/div[2]/table/tbody/tr[2]/td[8]/div/ul/li[2]/a').click()
    #删除互联云折扣
    bro.find_element_by_xpath('//*[@id="alterDiscount"]/div/table/tbody/tr[1]/td[4]/a[2]').click()
    time.sleep(1)
    #确定删除
    bro.find_element_by_xpath('//*[@id="deleteDiscount"]/div/div[2]/a[2]').click()
    time.sleep(5)
    #添加互联云折扣
    bro.find_element_by_xpath('//*[@id="alterDiscount"]/div/div[3]/a').click()
    time.sleep(2)
    bro.find_element_by_xpath('//*[@id="addDiscount"]/div/ul/li[3]/div[2]/input').send_keys('9')
    bro.find_element_by_xpath('//*[@id="addDiscount"]/div/div[2]/a[2]').click()
    time.sleep(2)
    bro.find_element_by_xpath('//*[@id="alterDiscount"]/div/div[5]/a').click()

if __name__ == '__main__':
    login()


