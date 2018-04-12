#!/usr/bin/python

################# This script scrapes a URL and finds out all files of specific extention and then add it to array and displays it #############


import requests
import re
from bs4 import BeautifulSoup
#from termcolor import colored

r=requests.get("http://"+<local server ip >+"/FTC/")
c=r.content
print(c)
soup=BeautifulSoup(c,"html.parser")
#urls = soup.body.find_all(text='.7z')
urls=[]
urls1=[]
z=[]
y=[]
for a in soup.find_all('a', href=True):
    #print ("Found the URL:", a['href'])
    urls.append(a.text)
    

    zone=re.search( r'(.*).exe',str(a))
    z.append(zone)
  
    if zone:
       print ("zone.group() : "), zone.group()
       y.append(zone)
    else:
       print ("Nothing found!!")

#print(urls)
#print(urls1)
#print(z)
#print(y)


for b in y:
  print(b)
