# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def sendMessage_warning():
    server = smtplib.SMTP('smtp.163.com', 25)
    server.login('18730598972@163.com', 'weiAIchi1996.')
    msg = MIMEText('爬虫slave被封警告！请求解封！', 'plain', 'utf-8')
    msg['From'] = '18730598972@163.com <18730598972@163.com>'
    msg['Subject'] = Header(u'爬虫被封禁警告！', 'utf8').encode()
    msg['To'] = u'seven <475352780@qq.com>'
    server.sendmail('18730598972@163.com', ['475352780@qq.com'], msg.as_string())
