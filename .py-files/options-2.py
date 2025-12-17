import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.alnafi.com")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

time.sleep(2)
driver.quit()