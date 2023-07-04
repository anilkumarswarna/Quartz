import time
import timeit

from Utils.facebookLibrary import facebookLibrary

obj = facebookLibrary()
obj.launchChrome()

obj.max_window()
time.sleep(3)
obj.Facebook_Launch()
time.sleep(3)
obj.openUrl()
time.sleep(2)
obj.textVal_ByClsName()
obj.imgVal_ByClsName()
time.sleep(3)
obj.screen_Shot()
obj.faceBook_LogIN()
obj.feaceBook_Pass()
time.sleep(5)
obj.logIn_Button()
time.sleep(5)





