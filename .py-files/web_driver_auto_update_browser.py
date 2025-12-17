from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


path=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=path)

driver.get("https://www.alnafi.com")
driver.maximize_window()

web_title = driver.title
if web_title == "Al Nafi | Online Courses, Certificates, and Diplomas in Emerging Technologies":
    print(f"Yes , Title is Verified : {web_title}")
else:
    print(f"Yes , Title is Not Verified : {web_title}")

driver.quit()