from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://www.saucedemo.com")
time.sleep(3)

# Correct element IDs
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(3)

driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(3)

# Optional: Click login button
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME,'product_sort_container').send_keys("Price (low to high)")
time.sleep(3)
driver.maximize_window()
driver.quit()