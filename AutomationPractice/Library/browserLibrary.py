from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

class browserLibrary():
    def __init__(self):
        self.driver = None

    def launch_Chrome(self):
        self.driver = driver

    def max_Window(self):
        driver.maximize_window()

    def back(self):
        driver.back()


#Facebook LogIn

    def launch_WebPage(self,url):
        driver.get(url)

    # def login(self,class_name):
    #     driver.find_element(By.CLASS_NAME,class_name).click()
    #     time.sleep(5)

    def user_Name(self,Name,Email):
        driver.find_element(By.NAME,Name).send_keys(Email)

    def password(self,Id,password):
        driver.find_element(By.ID,Id).send_keys(password)

    def click(self,Name,xpath,id):
        #Facebook
        # driver.find_element(By.CLASS_NAME,Name).click()

        #Letscodeit
        driver.find_element(By.CLASS_NAME,Name).click()
        time.sleep(5)
        driver.find_element(By.XPATH,xpath).click()
        #Radio Button Click And Validation
        time.sleep(5)
        bmwradioBtn = driver.find_element(By.ID,id)
        print("is_selected value:'before' ", bmwradioBtn.is_selected())
        bmwradioBtn.click()
        time.sleep(3)
        bmwradioBtn.is_selected()
        print("is_selected value:'after' ", bmwradioBtn.is_selected())

        if (bmwradioBtn.is_selected() != True):
            print("if condition click executed")
            bmwradioBtn.click()

        if (bmwradioBtn.is_selected() == True):
            print("selected - PASS")
        else:
            print("Not selected - FAIL")


#Open Url and validating

    def open_Url(self,url,expRes):
        driver.get(url)
        current_url = driver.current_url
        actRes = current_url
        if (expRes == actRes):
            print("Current url is Matched :PASS ")
        else:
            print("Current url is not matched :FAIL")


#Text validation at current page

    def text_val(self,clsName,xpath):
        #Facebook Txt
        # actRes1 = driver.find_element(By.CLASS_NAME,clsName).text
        actRes2 = driver.find_element(By.XPATH,xpath).text
        print("Text is:",actRes2)
        # if(expRes1 == actRes2):
        #     print("Text is matched :PASS")
        # else:
        #     print("Text is not matched :FAIL")

#Image validation in current page

    def img_Val(self,clsName):
        Image = driver.find_element(By.CLASS_NAME,clsName).is_displayed()
        print("Image is displayes :",Image)

#screenshot current page
    def screen_shot(self):
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)
        driver.save_screenshot(r"C:\Users\DELL\Desktop\fb11.png")
        time.sleep(3)
        driver.back()
        actVar = driver.find_element(By.NAME, "login")

        time.sleep(3)
        actVar.screenshot(r"C:\Users\DELL\Desktop\a2.png")

        # actVar.send_keys("anilkumarswarna158@gmail.com")

