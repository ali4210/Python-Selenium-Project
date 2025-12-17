from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()

#driver.find_element(By.ID, "searchLanguage").send_keys("af")
my_select = driver.find_element(By.ID, "searchLanguage")
sel = Select(my_select)
#sel.select_by_value("af")
sel.select_by_visible_text('Latina')
time.sleep(5)
driver.quit()
