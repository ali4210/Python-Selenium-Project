from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.shwapno.com/?srsltid=AfmBOoqkFd6tXqsEy4Pn35wwyik70EH0KSdbqxAJHUthwvUhi_DTC9uU&msid=mhqf1wdoixs5qs6')
driver.maximize_window()
driver.implicitly_wait(5)

time.sleep(3)  # Let page fully load

menu_bar = driver.find_element(By.XPATH,'/html/body/header/div[2]/div/div[1]/div[2]/ul/li[7]/a')
actions = ActionChains(driver)
actions.move_to_element(menu_bar).perform()

time.sleep(2)  # Wait for dropdown

pop_menu = driver.find_element(By.XPATH,'/html/body/header/div[2]/div/div[1]/div[2]/ul/li[7]/ul/li[3]/a')

# Use JavaScript click instead of regular click
driver.execute_script("arguments[0].click();", pop_menu)

time.sleep(5)
driver.quit()