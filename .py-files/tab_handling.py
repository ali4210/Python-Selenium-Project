import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get('https://alnafi.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Wait for the LinkedIn link and click it
# This finds the LinkedIn link by looking for href containing 'linkedin'
#linkedin_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'linkedin')]")))
linkedin_link = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div/div[5]/div/div[3]/div[2]/a[4]")))
linkedin_link.click()

time.sleep(2)  # Give new tab time to open

wins = driver.window_handles
print(f"Total windows: {len(wins)}")
print(f"Window 0 (alnafi.com): {wins[0]}")
print(f"Window 1 (linkedin.com): {wins[1]}")
time.sleep(3)

# Switch to alnafi
driver.switch_to.window(wins[0])
print(f"Tab 0 Title: {driver.title}")
time.sleep(2)

# Switch to LinkedIn
driver.switch_to.window(wins[1])
print(f"Tab 1 Title: {driver.title}")

time.sleep(5)
driver.quit()