import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.alert import Alert  # Add this import
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/div[2]/form/button').click()
alert_handle = Alert(driver)

print(alert_handle.text)

time.sleep(5)

alert_handle.accept()

time.sleep(5)

driver.quit()
