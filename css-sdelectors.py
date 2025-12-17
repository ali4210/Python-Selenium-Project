from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&dsh=S-503015602%3A1762481623445243&ifkv=ARESoU0YOvlaeil5Z5N9FwT1l5Zxn6I-xka0BAvBSxIuNlmeoWvPmO2H5X5L2tpHLcgAjWoLR5yJ7Q&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
time.sleep(3)

# Correct element IDs

driver.find_element(By.CSS_SELECTOR, "input[id='identifierId']").send_keys("saleemali")




time.sleep(3)

driver.maximize_window()
driver.quit()
'''
driver.find_element(By.CSS_SELECTOR, "#identifierId").send_keys("saleemali")
driver.find_element(By.CSS_SELECTOR, "input#identifierId").send_keys("saleemali")'''