import requests
import api_key
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

time,key=api_key.obfuscateApiKey()
payload={"apiKey":str(key),"username":"admin@shaunakd.com","password":"admin","timestamp":str(time)}
headers = {"content-type":"application/json"}
r = requests.post("https://10.10.104.23/zsapi/v1/authenticatedSession",data=json.dumps(payload),headers=headers,verify=False)
print r.content,r.status_code,r.headers,r.cookies
