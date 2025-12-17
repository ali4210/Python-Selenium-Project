import os
import time as t
from datetime import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://alnafi.com/")
driver.maximize_window()
driver.implicitly_wait(5)

def my_file_sc(driver):
    my_path = os.getcwd() + "\\"
    file_name = my_path+ t.asctime().replace(":","_")+".png"
    driver.save_screenshot(file_name)

t.sleep(5)

total_width = driver.execute_script("return document.body.scrollWidth")
total_height = driver.execute_script("return document.body.scrollHeight")
print(total_width,total_height)
driver.set_window_size(total_width,total_height)

t.sleep(0.5)
my_file_sc(driver)

driver.close()
driver.quit()


