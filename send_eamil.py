

#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_eamil(contant):
    sender = '15952430023@163.com'
    receiver = 'zhouss@syscloud.cn'
    subject = '测试结果'
    smtpserver = 'smtp.163.com'
    username = '15952430023@163.com'
    password = 'zhouss123'

    msg = MIMEText(contant,'plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = 'zhouss<15952430023@163.com>'
    msg['To'] = "zhouss@syscloud.cn"
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()





'''
#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '15952430023@163.com'
receiver = 'zhouss@syscloud.cn'
subject = 'zhouss'
smtpserver = 'smtp.163.com'
username = '15952430023@163.com'
password = 'zhouss123'

msg = MIMEText('zhouss','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
'''