#!/usr/bin/python
import smtplib
smtpObj=smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('shaunak7237@gmail.com','shaunak7237')
smtpObj.sendmail('shaunak7237@gmail.com','shaunak7237@gmail.com','Subject : So this is a general test')
smtpObj.quit()
