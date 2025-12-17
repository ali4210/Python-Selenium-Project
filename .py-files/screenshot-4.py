import os
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

def my_file_sc(driver):
    my_path = os.getcwd() + "\\"
    file_name = my_path+ t.asctime().replace(":","_")+".png"
    driver.save_screenshot(file_name)

t.sleep(5)
my_email = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/form/div[1]/div/div/input")
my_pass = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/form/div[2]/div/div/input")

driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_email)
driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_pass)

my_file_sc(driver)

driver.close()
driver.quit()


