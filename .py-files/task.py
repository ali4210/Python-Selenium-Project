import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

options_tag = driver.find_elements(By.TAG_NAME,"option")
for i in options_tag:
    print("Text is ",i.text, "The languages is ",i.get_attribute("lang"))
    print(len(options_tag))

driver.quit()