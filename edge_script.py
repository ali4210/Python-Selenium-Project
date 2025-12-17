from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os

# Set offline mode or use cached driver
os.environ['WDM_LOCAL'] = '1'
os.environ['WDM_SSL_VERIFY'] = '0'

try:
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)

    driver.get("https://www.alnafi.com")
    driver.maximize_window()

    web_title = driver.title
    expected_title = "Al Nafi | Online Courses, Certificates, and Diplomas in Emerging Technologies"

    if web_title == expected_title:
        print(f"Yes, Title is Verified: {web_title}")
    else:
        print(f"No, Title is Not Verified. Expected: '{expected_title}', Actual: '{web_title}'")

except Exception as e:
    print(f"Error: {e}")
    print("Please try manual driver installation as described in the comments")

finally:
    if 'driver' in locals():
        driver.quit()