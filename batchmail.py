#!/usr/bin/env python
# -*- coding: utf8 -*-

import smtplib
from email.mime.text import MIMEText
import time
import conf

mail_body = conf.MAIL_BODY
mail_from = conf.MAIL_FROM
mail_to = conf.MAIL_TO
mail_title = conf.MAIL_TITLE

def send_mail(_from, to_list, title, content):
    smtp = smtplib.SMTP()
    smtp.connect(conf.SMTP_SVR)
    smtp.login(conf.USER, conf.PWD)

    for to_item in to_list:
        msg = MIMEText(content)
        msg['Subject'] = title
        msg['From'] = _from
        msg['To'] = ''
        msg['To'] = to_item
        smtp.sendmail(mail_from, to_item, msg.as_string())
        print '%s send ok' % (to_item)
        time.sleep(0.01)
    smtp.quit()

if __name__ == '__main__':
    send_mail(mail_from, mail_to, mail_title, mail_body)
    print 'send ok'
