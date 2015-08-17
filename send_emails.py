#!/usr/bin/env python
# encoding: utf-8

import smtplib
from email.mime.text import MIMEText
from config import mailto_list,mail_host,mail_user,mail_pass



def send_mail(sub,content,to_list=mailto_list):
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = mail_user
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(mail_user, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    content =  '''
<html><body>
<h1>Hello</h1>
<p>send by <a href="http://www.python.org">Python</a>...</p>
</body></html>
'''
    if send_mail(mailto_list,"hello",content):
        print "发送成功"
    else:
        print "发送失败"

