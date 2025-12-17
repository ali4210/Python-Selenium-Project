import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.alnafi.com/")
driver.maximize_window()


def is_element_present(att,abd):

        if len(driver.find_elements(by=att, value=abd)) == 0:
            return False
        else:
            return True


print(is_element_present(By.XPATH,'saleemali'))
print(is_element_present(By.TAG_NAME,'a'))
print(is_element_present(By.TAG_NAME,'div'))

driver.quit()
