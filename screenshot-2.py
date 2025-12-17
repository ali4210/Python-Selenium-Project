import time as t
from datetime import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://alnafi.com/auth/sign-in")
driver.maximize_window()
driver.implicitly_wait(5)

t.sleep(0.4)
day = date.today()
date_time=datetime.now()
date_format=day.strftime("%B_%d_%Y")

time_format=date_time.strftime("%I_%M_%p")
myfile = "Screenshot__"+date_format+"_"+time_format+".png"



my_email = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/form/div[1]/div/div/input")
my_pass = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/form/div[2]/div/div/input")

driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_email)
driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_pass)
#driver.get_screenshot_as_file(myfile)
driver.get_screenshot_as_file('./screenshot//'+myfile)
driver.get_screenshot_as_file(r"C:\Users\User\Desktop\\"+myfile)
driver.close()
driver.quit()


