from selenium import webdriver
from Library.browserLibrary import browserLibrary

obj = browserLibrary()

class letscodeItlibrary():

    def __init__(self):
        pass

    def chrome_Browser(self):
        obj.launch_Chrome()

    def launch_WebPage(self):
        obj.launch_WebPage("https://www.letskodeit.com/login")

    def maximize_Window(self):
        obj.max_Window()

    def url_Validation(self):
        #Letskodeit
        obj.open_Url("https://www.letskodeit.com/practice",expRes="https://www.letskodeit.com/practice")

    # def login(self):
    #     obj.login("dynamic-link")

    def user_Name(self):
        obj.user_Name("email","anilswarna1995@gmail.com")

    def passWord(self):
        obj.password("login-password","SAnil@155")

    def button(self):
        obj.click("btn","/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[2]/ul[1]/li[6]/a[1]","bmwradio")

    def text_val(self):
        obj.text_val("/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h1[1]")
