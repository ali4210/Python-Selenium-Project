import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://admin-demo.nopcommerce.com/Admin/Order/List")
driver.maximize_window()

my_email = driver.find_element(By.ID,"Email")
my_email.clear()
time.sleep(2)
my_email.send_keys('admin@yourstore.com')

my_password = driver.find_element(By.ID,"Password")
my_password.clear()
time.sleep(2)
my_password.send_keys('admin')

time.sleep(2)
driver.find_element(By.ID, 'RememberMe').click()

time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[6]/main/div/section/div/div[2]/div[1]/div/form/div[3]/button').click()

time.sleep(3)

def is_element_present(att,abd):
    if len(driver.find_elements(by=att,value=abd)) == 0:
        return False
    else:
        return True
#method-1
i=1
while is_element_present(By.XPATH,'/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[3]/table/tbody/tr['+str(i)+']/td[1]/input'):
    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[3]/table/tbody/tr['+str(i)+']/td[1]/input').click()
    time.sleep(2)
    i = i+1
print("Total checkbox value is : ", len(driver.find_elements(By.CLASS_NAME,'checkboxGroups')))


#method-2
#driver.find_element(By.XPATH,'/html/body/div[3]/nav/ul/li/a/i').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/nav/ul/li[4]/a').click()
driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/nav/ul/li[4]/ul/li[1]/a/p').click()
time.sleep(2)

my_checkboxes = driver.find_elements(By.NAME,'checkbox_customers')
for checkbox in my_checkboxes:
    checkbox.click()
    time.sleep(2)
print("Total checkbox value is:", len(driver.find_elements(By.NAME,'checkbox_customers')))


driver.quit()
