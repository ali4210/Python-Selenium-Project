from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.implicitly_wait(20)
wait = WebDriverWait(driver, 10)

driver.get("https://workspace.google.com/intl/en-US/gmail/")
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()
driver.find_element(By.ID, 'identifierId').send_keys('saleemali.mohammad')
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()

action = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'Passwd')))
action.send_keys('Alisaleem01627609670')
login = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/span')))
login.click()
#driver.find_element(By.NAME, 'Passwd').send_keys('Alisaleem01627609670')
#driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()

print("Login Success")
driver.quit()
