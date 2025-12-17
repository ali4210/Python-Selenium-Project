import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

firefox_options = Options()
firefox_options.headless = True


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.alnafi.com/")
driver.maximize_window()
driver.implicitly_wait(5)

time.sleep(0.4)


#driver.save_screenshot("mylogin.png")
#driver.save_screenshot('mylogin2.jpeg')
#driver.get_screenshot_as_file('./screenshot/mylogin3.png')
#driver.get_screenshot_as_file(r"C:\Users\User\Pictures\Screenshots\mylogin3.png")
#print(driver.get_screenshot_as_png())

my_section = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[10]/div/img')
my_section.screenshot('visa5.png')

time.sleep(2)

driver.quit()