import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities # Still need this if using older syntax, but we'll use Options
from selenium.webdriver.chrome.options import Options as ChromeOptions # Import specific Options class
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


hub_url = "http://10.0.2.1:4444/wd/hub"

# 1. DEFINE THE BROWSER OPTIONS
# This step replaces the 'desired_capabilities' dictionary directly.
chrome_options = ChromeOptions()

# 2. CREATE THE REMOTE DRIVER
# Note: For Selenium 4, the options are passed directly via the 'options' argument.
# We are creating the remote driver that will talk to your Grid Hub.
driver = webdriver.Remote(
    command_executor=hub_url,
    options=chrome_options # <-- CORRECT ARGUMENT for modern Selenium
)


# ----------------------------------------------------
# NOTE: You were creating a SECOND driver instance locally, which is likely not what you intended
# For a Grid test, you usually only want the Remote driver.
# If you run the code below, it will overwrite the Grid connection:
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# ----------------------------------------------------


driver.get("https://google.com")

driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
time.sleep(5)
driver.quit()


###RUN in Pycharm terminal
# java -jar .\selenium-server-4.38.0.jar hub
###RUN in Windows Terminal
# java -jar .\selenium-server-4.38.0.jar node --detect-drivers true --publish-events tcp://10.0.2.1:4442 --subscribe-events tcp://10.0.2.1:4443