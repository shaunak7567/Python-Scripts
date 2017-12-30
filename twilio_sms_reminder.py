#!/usr/bin/python
from twilio.rest import Client
accountSID='AC69ad35195752b759537ed23caa430e0d'
authToken='e1bf9e1fb6bbfaa69b1901a570231328'
twiliocli=Client(accountSID,authToken)
mytwilionumber='+18316091347'
mycellphone='+14084807851'
message=twiliocli.messages.create(body='HI! This is a test message from shaunak!', from_=mytwilionumber,to=mycellphone)
print(message.sid)
