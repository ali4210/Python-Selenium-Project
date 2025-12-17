from selenium import webdriver
from selenium.webdriver import ActionChains  # This is what you need
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://alnafi.com/courses')
driver.maximize_window()
driver.implicitly_wait(5)

# Changed from find_elements to find_element
my_path = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div/div[1]/div/a/div/div/div[2]/div/div[1]/div[2]')

# Create ActionChains instance
actions = ActionChains(driver)
actions.context_click(my_path).perform()

time.sleep(5)
driver.quit()

