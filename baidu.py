#coding = utf-8
from selenium import webdriver
import time
import xlrd
from selenium.webdriver.common.action_chains import ActionChains

#search_text = {'text','selenium','犀思云'}
'''
data = open('data.txt','r')
list=[]
lines = data.readlines()
for line in lines:
    key = line.split('=')[0]
    val = line.split('=')[1]
    list.append(val)
data.close()
'''

data = xlrd.open_workbook('e:\\test.xlsx')
table = data.sheet_by_name(u'Sheet1')
print(table.col_values(0))
list = []
for text in table.col_values(0):
    list.append(text)


for text in list:
    bro = webdriver.Firefox()
    bro.get('https://www.baidu.com/')
    kw = bro.find_element_by_id('kw')
    kw.send_keys(text)
    bro.find_element_by_id('su').click()
    time.sleep(1)
    print(text)
    bro.close()


#截图
#bro.get_screenshot_as_file('d:\\a.png')
#btn = bro.find_element_by_id('su')
#btn.click()
#bro.refresh()

#con = bro.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/a[1]')
#con = bro.find_element_by_link_text('新闻')
#con.click()
#print(con.text)
'''
hover = bro.find_element_by_link_text('更多产品')
print(hover)
ActionChains(bro).move_to_element(hover).perform()
'''