#!/usr/bin/env python
# -*- coding: utf8 -*-

import smtplib
from email.mime.text import MIMEText
import conf

mail_body = conf.MAIL_BODY
mail_from = conf.MAIL_FROM
mail_to = conf.MAIL_TO
mail_title = conf.MAIL_TITLE

def send_mail(_from, to_list, title, content):
    msg = MIMEText(content)
    msg['Subject'] = title
    msg['From'] = _from
    msg['To'] = ';'.join(to_list)

    smtp = smtplib.SMTP()
    smtp.connect(conf.SMTP_SVR)
    smtp.login(conf.USER, conf.PWD)
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    send_mail(mail_from, mail_to, mail_title, mail_body)
    print 'send ok'
