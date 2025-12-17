from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time  # optional, just to let you see it before quitting

# Create a Service object with ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Initialize Chrome with the service
driver = webdriver.Chrome(service=service)
driver.get("https://alnafi.com/auth/sign-in")
my_username=driver.find_element(By.NAME, "email")
my_username.send_keys("saleemali.mohammad@gmail.com")

my_password = driver.find_element(By.NAME, "password")
my_password.send_keys("Alisaleem01627609670")


login_button = driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/div[2]/div[1]/div/form/button")
login_button.click()

time.sleep(10)
driver.quit()


