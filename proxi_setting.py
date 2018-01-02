from selenium.webdriver.common.proxy import *
from selenium import webdriver
myProxy = "10.66.63.45:9443"
'''
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })
driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver',proxy=proxy)
driver.get("http://www.google.com")


'''

'''
##### Set the proxy as production zscaler.net ##########

profile = webdriver.FirefoxProfile() 
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "gateway.zscaler.net")
profile.set_preference("network.proxy.http_port", 10085)

profile.update_preferences() 
driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver',firefox_profile=profile)

driver.get("http://10.65.1.220")
'''



''' 
This function below is a correct working function as of now
'''

class proxy_creator:
    def set_proxy(self):
        self.profile = webdriver.FirefoxProfile() 
        self.profile.set_preference("network.proxy.type", 1)
        self.profile.set_preference("network.proxy.http", "gateway.zscaler.net")
        self.profile.set_preference("network.proxy.http_port", 9443)
        self.profile.set_preference("browser.cache.disk.enable", False)
        self.profile.set_preference("browser.cache.memory.enable", False)
        self.profile.set_preference("browser.cache.offline.enable", False)
        self.profile.set_preference("network.http.use-cache", False)
        self.profile.update_preferences() 
        self.driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver',firefox_profile=self.profile)
        

        self.driver.get("http://10.65.1.220")
        self.driver.manage.delete_all_cookies()



proxy_c=proxy_creator()
proxy_c.set_proxy()



