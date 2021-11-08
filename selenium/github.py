from githubUserInfo import username,password
from seleniummm import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.followers=[]

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)
        self.browser.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]")

    def getFollowers(self):
        self.browser.get("https://github.com/asbet?tab=followers")
        time.sleep(2)

        items=self.browser.find_element_by_css_selector(".d-table.table-fixed")

       #YARIM KALDI


github=Github(username,password)
github.signIn()





