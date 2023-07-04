# # # frames/iframes
# #
# #
# # from selenium.webdriver.common.by import By
# # from selenium import webdriver
# # import time
# # from selenium.webdriver.support.select import Select
# #
# # driver = webdriver.Edge()
# #
# # url = "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html"
#
# # driver.get(url)
# #
# # driver.maximize_window()
# # #
# #
# # driver.switch_to.frame("packageListFrame")
# # driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
# #
# # time.sleep(2)
# #
# # driver.switch_to.default_content()
# # driver.switch_to.frame("packageFrame")
# # driver.find_element(By.XPATH,"//span[normalize-space()='Alert']").click()
# #
# # time.sleep(2)
# # driver.switch_to.default_content()
# # driver.switch_to.frame("packageListFrame")
# # driver.find_element(By.LINK_TEXT,"org.openqa.selenium.bidi").click()
# # time.sleep(2)
# #
# # driver.switch_to.default_content()
# # driver.switch_to.frame("packageFrame")
# # driver.find_element(By.LINK_TEXT,"BiDi").click()
# # time.sleep(2)
# #
# # driver.switch_to.default_content()
# # driver.switch_to.frame("classFrame")
# # driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[2]/a").click()
# #
# #
# # time.sleep(5)
# # driver.quit()
#
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Edge(r"C:\Users\user\PycharmProjects\browser1\msedgedriver.exe")

url = "https://www.letskodeit.com/practice"


# url = "https://www.facebook.com/"

driver.get(url)
time.sleep(4)

driver.maximize_window()

time.sleep(3)
#
#
# #----------------------------------  xPath   ------------------------
#
# #Dynamic web elemnts..so we have to use xPath locator..only diff is name of the elemnt
#
# #Relative xpath
# driver.find_element(By.XPATH, '//input[@id="email"]').send_keys("relative@gmail.com")
# #Absolute xpath
# driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys("absolte@gmail.com")
# time.sleep(10)
# driver.find_element(By.CSS_SELECTOR,"input#email").clear()
# driver.find_element(By.CSS_SELECTOR,"input#pass").clear()
#
# #Starts-with
# driver.find_element(By.XPATH, '//*[starts-with(@id,"email")]').send_keys("starts-wtih@gmail.com")
# #Contains
# driver.find_element(By.XPATH, '//input[contains(@id,"pass")]').send_keys("contains@gmail.com")
# time.sleep(2)
# driver.find_element(By.XPATH, '//div[contains(@class,"_9lsa")]').click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input#pass").clear()
# driver.find_element(By.CSS_SELECTOR,"input#email").clear()
#
# #OR
# driver.find_element(By.XPATH, "//input[@id='email1' or @class='inputtext _55r1 _6luy']").send_keys("or@gmail.com")
#
# #AND
# driver.find_element(By.XPATH, "//input[@id='pass' and @name='pass']").send_keys("and@gmail.com")
# time.sleep(10)
#
# #text()
# driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()
#
#
# time.sleep(5)
# driver.quit()

driver.find_element(By.ID,"carselect").click()
time.sleep(4)

# act_res=driver.find_element(By.XPATH,"//*[@id=radio-btn-example]/fieldset/legend").text
# print("actual result is :",act_res)
# time.sleep(4)


