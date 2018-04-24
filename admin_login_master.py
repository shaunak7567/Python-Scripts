from requests import Session
import time
import json
from bs4 import BeautifulSoup
import argparse
import time
import logging
import socket
import ast
from collections import defaultdict


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')


class admin_login():



    def get_user_input(self) :
        logging.debug('Start of the program')
        self.parser = argparse.ArgumentParser(description='Description of required arguments')

        #2) Add Arguments

        # Required positional argument
        logging.debug('input username')
        self.parser.add_argument('un',
        help = 'Enter your Admin UI login username')

        # Required positional argument
        logging.debug('input pw')
        self.parser.add_argument('pw',help = 'Enter your Admin UI login password')

        # Required argument
        logging.debug('input cname')
        self.parser.add_argument('cname', help='Enter your Admin UI cloudname or IP address')

    #    3) Parse

        self.args = self.parser.parse_args()

        #4) Access

        print("Argument values:")
        logging.info('uname entered - >'+ self.args.un)
        logging.info('pw entered - >' + self.args.pw)
        logging.info('cname entered - >' + self.args.cname)




    def obfuscateApiKey(self) :
        self.seed = 'jj7tg80fEGao'
        self.now = str(int(time.time() * 1000))
        self.n = self.now[-6:]
        self.r = str(int(self.n) >> 1).zfill(6)
        self.key = ""
        for i in range(0, len(self.n), 1):
          self.key += self.seed[int(self.n[i])]
        for j in range(0, len(self.r), 1):
          self.key += self.seed[int(self.r[j])+2]
        print ("Timestamp:%s     Key:%s" % (self.now, self.key))
        return (self.now,self.key)






    def create_url_filtering_rule(self):
        self.s = Session()
        # URL1="https://10.10.104.23/zsapi/v1/authenticatedSession"
        # URL2="https://10.10.104.23/zsapi/v1/webApplicationRules"

        print(type(self.args.cname))
        auth_url = "https://" + self.args.cname + "/zsapi/v1/authenticatedSession"
        url_type_url = "https://" + self.args.cname + "/zsapi/v1/urlFilteringRules"
        activate_url= "https://" + self.args.cname + "/zsapi/v1/orgAdminStatus/activate"


        self.time, self.key = self.obfuscateApiKey()

        payload = {"apiKey": str(self.key), "username": self.args.un, "password": self.args.pw,
                   "timestamp": str(self.time)}
        headers = {"content-type": "application/json"}
        self.r = self.s.post(auth_url, data=json.dumps(payload), headers=headers, verify=False)
        print(self.r.cookies)
        print(self.r.cookies['JSESSIONID'])
        print(self.r.cookies['ZS_SESSION_CODE'])


        ZS_CUSTOM_CODE = self.r.cookies['ZS_SESSION_CODE']
        print(ZS_CUSTOM_CODE)

        for num in range(1, 2):

          print(type(num))
          payload1 = {"name":"URL_Filtering_"+str(num),"protocols":["FOHTTP_RULE","FTP_RULE","HTTPS_RULE","HTTP_RULE","SSL_RULE","TUNNEL_RULE"],"id":101966,"order":num,"urlCategories":["ADULT_SEX_EDUCATION","ADULT_THEMES","K_12_SEX_EDUCATION","LINGERIE_BIKINI","NUDITY","OTHER_ADULT_MATERIAL","PORNOGRAPHY","SEXUALITY","SOCIAL_ADULT"],"state":"ENABLED","rank":7,"requestMethod":"ALL","blockOverride":"false","action":"BLOCK","protocolSelection":["FOHTTP_RULE","FTP_RULE","HTTPS_RULE","HTTP_RULE","SSL_RULE","TUNNEL_RULE"]}

          # soup = BeautifulSoup(s.get(URL1).text, "html.parser")
          # print(soup)
          # csrf = soup.find(name="csrftoken")
          # print(csrf)
          headers = {"content-type": "application/json", "zs_custom_code": ZS_CUSTOM_CODE}
          # x = s.post(URL2, data=json.dumps(payload1), headers=headers, verify=False,cookies=r.cookies)
          self.x = self.s.post(url_type_url, data=json.dumps(payload1), headers=headers, verify=False)
          print(self.x.headers)
          print(self.x.content)
          print(self.x.status_code)

        ########## Activate function ##############
        activate_payload= {"adminActivateStatus": "ADM_ACTV_DONE"}
        headers = {"content-type": "application/json", "zs_custom_code": ZS_CUSTOM_CODE}
        # x = s.post(URL2, data=json.dumps(payload1), headers=headers, verify=False,cookies=r.cookies)
        self.x = self.s.put(activate_url, data=json.dumps(activate_payload), headers=headers, verify=False)
        print(self.x.headers)
        print(self.x.content)
        print(self.x.status_code)

        ########## Delete function ##############
        delete_url = "https://" + self.args.cname + "/zsapi/v1/urlFilteringRules/" + str(101984)
        print(delete_url)
        headers = {"content-type": "application/json", "zs_custom_code": ZS_CUSTOM_CODE}
        # x = s.post(URL2, data=json.dumps(payload1), headers=headers, verify=False,cookies=r.cookies)
        self.x = self.s.delete(delete_url, data=json.dumps(""), headers=headers, verify=False)
        print(self.x.headers)
        #print(self.x.content)
        print(self.x.status_code)


        ########## GET function ##############

        get_url = "https://" + self.args.cname + "/zsapi/v1/urlFilteringRules/"
        print(delete_url)
        #get_payload=[{"accessControl":"READ_WRITE","name":"URL_Filtering_1","protocols":["FOHTTP_RULE","FTP_RULE","HTTPS_RULE","HTTP_RULE","SSL_RULE","TUNNEL_RULE"],"id":101985,"order":1,"urlCategories":["OTHER_ADULT_MATERIAL","ADULT_THEMES","LINGERIE_BIKINI","NUDITY","PORNOGRAPHY","SEXUALITY","ADULT_SEX_EDUCATION","K_12_SEX_EDUCATION","SOCIAL_ADULT"],"state":"ENABLED","rank":7,"requestMethod":"ALL","blockOverride":false,"action":"ALLOW"}]
        headers = {"content-type": "application/json", "zs_custom_code": ZS_CUSTOM_CODE}
        # x = s.post(URL2, data=json.dumps(payload1), headers=headers, verify=False,cookies=r.cookies)
        self.x = self.s.get(get_url, data=json.dumps(""), headers=headers, verify=False)
        print("Header values are - >>>" +str(self.x.headers))

        print("Content Values are -- >>>" +str(self.x.content))
        print("Status Code is -- >>" + str(self.x.status_code))


        ##### Once you get it , we nned to decode it, convert it to a dictionary, then we can access its elements ####

        self.recvd_data=self.x.content.decode("utf-8")
        print(self.recvd_data)

        #recvd_data1 = ast.literal_eval(recvd_data)
        #print(recvd_data1['name'])

        self.recvd_data1 = json.loads(self.recvd_data)
        print(self.recvd_data1)

        lst=lambda:list(self.recvd_data1)

        self.d=defaultdict(lst)
        print(type(self.d))

        #print("The ID received from GET request is : - > " +str(d['id']))

        self.new_dict={}
        for element in self.d:
            for k, v in element.items():
                self.new_dict[k] = v

        print(type(self.new_dict))
        #print(new_dict['name'])

        self.keys1=self.new_dict.keys()
        print(self.keys1)



        ##### Stuck at converting list to dictionary

        #print(recvd_data)
        #print("ID extracted from the GET request is -- >>" + str(self.x.content["accessControl"]))




    def create_cloudapp_rule(self):
        self.s = Session()
        #URL1="https://10.10.104.23/zsapi/v1/authenticatedSession"
        #URL2="https://10.10.104.23/zsapi/v1/webApplicationRules"

        print(type(self.args.cname))
        URL1 = "https://"+self.args.cname+"/zsapi/v1/authenticatedSession"
        URL2 = "https://"+self.args.cname+"/zsapi/v1/webApplicationRules"

        #print(URL1,URL2)

        self.time,self.key=self.obfuscateApiKey()

        payload={"apiKey":str(self.key),"username":self.args.un,"password":self.args.pw,"timestamp":str(self.time)}
        headers = {"content-type":"application/json"}
        self.r = self.s.post(URL1,data=json.dumps(payload),headers=headers,verify=False)
        print(self.r.cookies)
        print (self.r.cookies['JSESSIONID'])
        print(self.r.cookies['ZS_SESSION_CODE'])

        ZS_CUSTOM_CODE=self.r.cookies['ZS_SESSION_CODE']
        print(ZS_CUSTOM_CODE)

        #"id": 100487,
        payload1 = { "id": 100487,"type": "FILE_SHARE", "order": 1,
                    "actions": ["ALLOW_FILE_SHARE_VIEW", "DENY_FILE_SHARE_UPLOAD"], "state": "ENABLED", "rank": 7,
                    "name": "File_Sharing_5"}

        #soup = BeautifulSoup(s.get(URL1).text, "html.parser")
        #print(soup)
        #csrf = soup.find(name="csrftoken")
        #print(csrf)
        headers = {"content-type": "application/json","zs_custom_code":ZS_CUSTOM_CODE}
        #x = s.post(URL2, data=json.dumps(payload1), headers=headers, verify=False,cookies=r.cookies)
        self.x = self.s.post(URL2, data=json.dumps(payload1), headers=headers, verify=False)
        print(self.x.headers )
        print (self.x.content )
        print(self.x.status_code )



    def create_filetype_rule(self):
        self.s = Session()
        # URL1="https://10.10.104.23/zsapi/v1/authenticatedSession"
        # URL2="https://10.10.104.23/zsapi/v1/webApplicationRules"

        print(type(self.args.cname))
        URL1 = "https://" + self.args.cname + "/zsapi/v1/authenticatedSession"
        URL2 = "https://" + self.args.cname + "/zsapi/v1/fileTypeRules"

        # print(URL1,URL2)

        self.time, self.key = self.obfuscateApiKey()

        payload = {"apiKey": str(self.key), "username": self.args.un, "password": self.args.pw,
                   "timestamp": str(self.time)}
        headers = {"content-type": "application/json"}
        self.r = self.s.post(URL1, data=json.dumps(payload), headers=headers, verify=False)
        print(self.r.cookies)
        print(self.r.cookies['JSESSIONID'])
        print(self.r.cookies['ZS_SESSION_CODE'])

        ZS_CUSTOM_CODE = self.r.cookies['ZS_SESSION_CODE']
        print(ZS_CUSTOM_CODE)

        # "id": 100487,
        payload1 = {"id":101962,"protocols":["FOHTTP_RULE","FTP_RULE","HTTPS_RULE","HTTP_RULE"],"order":1,"fileTypes":["P7Z","BZIP2","CAB","GZIP","ISO","RAR","STUFFIT","TAR","ZIP","SCZIP"],"filteringAction":"ALLOW","operation":"DOWNLOAD","state":"ENABLED","rank":7,"name":"File_Type_1","protocolSelection":["FOHTTP_RULE","FTP_RULE","HTTPS_RULE","HTTP_RULE"]}

        # soup = BeautifulSoup(s.get(URL1).text, "html.parser")
        # print(soup)
        # csrf = soup.find(name="csrftoken")
        # print(csrf)
        headers = {"content-type": "application/json", "zs_custom_code": ZS_CUSTOM_CODE}
        # x = s.post(URL2, data=json.dumps(payload1), headers=headers, verify=False,cookies=r.cookies)
        self.x = self.s.post(URL2, data=json.dumps(payload1), headers=headers, verify=False)
        print(self.x.headers )
        print(self.x.content)
        print(self.x.status_code )

if __name__ == '__main__':

    logging.debug('Creating object of Admin_login class')
    adm_login=admin_login()
    logging.debug('Calling get user input method with new login class')
    adm_login.get_user_input()
    #logging.debug('Calling create cloud app rule')
    #adm_login.create_cloudapp_rule()

    #logging.debug('Calling create filetype rule')
    #adm_login.create_filetype_rule()

    logging.debug('Calling create URL Filtering rule')
    adm_login.create_url_filtering_rule()


