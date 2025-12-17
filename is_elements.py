import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

def is_element_present(tag_name):
    try:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://www.alnafi.com/")
        driver.maximize_window()

        a_tag = driver.find_element(By.TAG_NAME,tag_name)
        return True
    except:
        return False


print(is_element_present('a'))
