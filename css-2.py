

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://alnafi.com/auth/sign-in")
time.sleep(3)

# Correct element IDs

driver.find_element(By.CSS_SELECTOR, "a[href='/auth/sign-up']").click()




time.sleep(3)

driver.maximize_window()
driver.quit()
'''
driver.find_element(By.CSS_SELECTOR, "#identifierId").send_keys("saleemali")
driver.find_element(By.CSS_SELECTOR, "input#identifierId").send_keys("saleemali")
driver.find_element(By.CSS_SELECTOR, "input[href='/auth/sign-up']").click()'''

#XPATH
#//input[@*]
#//input[@id='Username/ Email']
#//*[@ id]
#//*[@ id][@class]
#//*[@ id and @class]
#//*[contains(text(),'Create account')]
#//div[@class="VfPpkd-dgl2Hf-ppHlrf-sM5MNb"]/div[1]
#//div[@class]/div[1]
#//div[@class]/div[3]
#//div[@class]/div[3]/../..
#//div[@class="aCsJod oJeWuf"]/self::div
#//div[@class="aCsJod oJeWuf"]/ancestor::div
#//div[@class="aCsJod oJeWuf"]/parent::div
#//div[@class="aCsJod oJeWuf"]/descendant::div
#//div[@class="aCsJod oJeWuf"]/descendant::*
#//div[@class="aCsJod oJeWuf"]/child::div
#//div[@class="aCsJod oJeWuf"]/div/div/div
#//div[@class="aCsJod oJeWuf"]/div/div/div[@class]/parent::div
#//div[@class="aCsJod oJeWuf"]/div/div/preceding-sibling::div
#//div[@class="aCsJod oJeWuf"]/div/div/following-sibling::div

#//html/body/div[1]/div/div/div[2]