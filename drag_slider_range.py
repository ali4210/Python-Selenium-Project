from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get(
    "https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&otracker=nmenu_sub_Men_0_Clothing")
driver.maximize_window()
driver.implicitly_wait(5)

time.sleep(3)  # Let page fully load

actions = ActionChains(driver)
slider_bar = driver.find_element(By.XPATH, '/html/body/div/div/div[3]')
actions.drag_and_drop_by_offset(slider_bar,-50,0).perform()

time.sleep(5)
driver.quit()
