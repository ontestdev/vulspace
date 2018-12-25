#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_eamil(contant):
    sender = '15952430023@vulspace.com'
    receiver = 'zhouss@vulspace.cn'
    subject = '测试结果'
    smtpserver = 'smtp.vulspace.com'
    username = '15952430023@vulspace.com'
    password = 'zhouss123'

    msg = MIMEText(contant,'plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = 'zhouss<15952430023@vulspace.com>'
    msg['To'] = "zhouss@vulspace.cn"
    smtp = smtplib.SMTP()
    smtp.connect('smtp.vulspace.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
