import time

from Library.browserLibrary import browserLibrary

obj = browserLibrary()

class facebookLibrary():

    def launchChrome(self):
        obj.launch_Chrome()

    def max_window(self):
        obj.max_Window()

    def Facebook_Launch(self):
        obj.launch_WebPage("https://www.facebook.com/")



    def openUrl(self):
        #Facebook
        obj.open_Url("https://www.facebook.com/",expRes="https://www.facebook.com/")
        #Letskodeit
        # obj.open_Url("https://www.letskodeit.com/practice",expRes="https://www.letskodeit.com/practice")


    def imgVal_ByClsName(self):
        obj.img_Val("_8ilh")

    def textVal_ByClsName(self):
        obj.text_val("_8eso","Facebook helps you connect and share with the people in your life.")

    def faceBook_LogIN(self):
        obj.user_Name("email","anilswarna1995@gmail.com")

    def feaceBook_Pass(self):
        obj.password("pass","SAnil@155")

    def logIn_Button(self):
        obj.click("_42ft")

    def screen_Shot(self):
        obj.screen_shot()




