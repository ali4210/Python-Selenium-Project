from selenium import webdriver
from selenium.webdriver.chrome.service import Service
path=Service(r"C:\Users\User\PycharmProjects\pythonProject3\Alnafi Selenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.alnafi.com")
