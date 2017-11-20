#coding = utf-8
from selenium import webdriver
import time


def login(user,pwd):
    bro = webdriver.Firefox()
    bro.get('http://192.168.211.99/naas/account/')

    print (bro.title)
    user_ele = bro.find_element_by_class_name('form-control')
    password_ele = bro.find_element_by_css_selector('input[type="password"]')
    time.sleep(1)
    user_ele.send_keys(user)
    time.sleep(1)
    password_ele.send_keys(pwd)
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
    time.sleep(3)
    bro.close()








