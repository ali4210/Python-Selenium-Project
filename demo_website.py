from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time  # optional, just to let you see it before quitting

# Create a Service object with ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Initialize Chrome with the service
driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com")
time.sleep(3)

# Correct element IDs
myusername = driver.find_element(By.ID, "user-name")
myusername.send_keys("standard_user")
time.sleep(3)

mypassword = driver.find_element(By.ID, "password")
mypassword.send_keys("secret_sauce")
time.sleep(3)

# Optional: Click login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

driver.maximize_window()

time.sleep(3)  # Pause to visually confirm before closing
driver.quit()
