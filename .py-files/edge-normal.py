
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Use Service class instead of executable_path
path = Service(r"C:\Users\User\PycharmProjects\pythonProject3\Alnafi Selenium\Drivers\msedgedriver.exe")
driver = webdriver.Edge(service=path)
driver.get("https://www.alnafi.com")
driver.maximize_window()

web_title = driver.title
if web_title == "Al Nafi | Online Courses, Certificates, and Diplomas in Emerging Technologies":
    print(f"Yes , Title is Verified : {web_title}")
else:
    print(f"Yes , Title is Not Verified : {web_title}")

driver.quit()