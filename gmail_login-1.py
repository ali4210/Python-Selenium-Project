from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import os


def human_type(element, text):
    """Type like a human with random delays between characters"""
    for character in text:
        element.send_keys(character)
        # Random delay between keystrokes (50-200ms)
        time.sleep(random.uniform(0.05, 0.2))


def random_delay(min_seconds=1, max_seconds=3):
    """Random delay between actions"""
    time.sleep(random.uniform(min_seconds, max_seconds))


def random_mouse_movement(driver):
    """Add random mouse movements to appear more human"""
    try:
        actions = ActionChains(driver)
        # Move to random positions on the screen
        for _ in range(random.randint(2, 4)):
            x_offset = random.randint(-100, 100)
            y_offset = random.randint(-50, 50)
            actions.move_by_offset(x_offset, y_offset)
            actions.perform()
            time.sleep(random.uniform(0.1, 0.3))
        # Reset mouse position
        actions.move_to_element(driver.find_element(By.TAG_NAME, 'body'))
        actions.perform()
    except:
        pass  # Ignore mouse movement errors


def setup_stealth_driver():
    """Setup Edge driver with stealth options"""
    edge_options = webdriver.EdgeOptions()

    # Remove automation indicators
    edge_options.add_argument("--disable-blink-features=AutomationControlled")
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    edge_options.add_experimental_option('useAutomationExtension', False)

    # Additional stealth settings
    edge_options.add_argument("--disable-extensions")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--disable-web-security")
    edge_options.add_argument("--allow-running-insecure-content")

    # Use Service class
    path = Service(r"C:\Users\User\PycharmProjects\pythonProject3\Alnafi Selenium\Drivers\msedgedriver.exe")
    driver = webdriver.Edge(service=path, options=edge_options)

    # Remove webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver


def login_gmail():
    """Main login function with human-like behavior"""
    driver = setup_stealth_driver()

    try:
        # Navigate to Gmail
        print("Navigating to Gmail...")
        driver.get("https://workspace.google.com/intl/en-US/gmail/")
        driver.maximize_window()

        # Random delay before first action
        random_delay(2, 4)

        # Random mouse movement before clicking
        random_mouse_movement(driver)

        # Click Sign in with explicit wait
        print("Clicking Sign in...")
        sign_in_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Sign in'))
        )

        # Move to element before clicking
        actions = ActionChains(driver)
        actions.move_to_element(sign_in_link).pause(random.uniform(0.5, 1.5)).click().perform()

        random_delay(2, 3)

        # Enter email with human-like typing
        print("Entering email...")
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'identifierId'))
        )

        # Random mouse movement before typing
        random_mouse_movement(driver)

        # Click on field and type with human-like delays
        actions.move_to_element(email_field).click().perform()
        random_delay(0.5, 1)
        human_type(email_field, 'saleemali.mohammad')

        random_delay(1, 2)

        # Click Next button
        print("Clicking Next after email...")
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))
        )

        # Move to button and click with slight delay
        actions.move_to_element(next_button).pause(random.uniform(0.3, 0.7)).click().perform()

        # Wait for password field with longer timeout
        print("Waiting for password field...")
        random_delay(3, 5)

        # Enter password with human-like behavior
        print("Entering password...")
        password_field = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.NAME, 'Passwd'))
        )

        # Random mouse movement before password
        random_mouse_movement(driver)

        # Type password with human-like behavior
        actions.move_to_element(password_field).click().perform()
        random_delay(0.5, 1)
        human_type(password_field, 'Alisaleem01627609670')

        random_delay(1, 2)

        # Click password Next button
        print("Clicking Next after password...")
        password_next = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))
        )

        actions.move_to_element(password_next).pause(random.uniform(0.3, 0.7)).click().perform()

        # Wait for login to complete with verification
        print("Waiting for login to complete...")
        random_delay(5, 8)

        # Check if login was successful
        try:
            # Look for inbox or any element that indicates successful login
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Inbox")) |
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'mail.google.com')]")) |
                EC.presence_of_element_located((By.CSS_SELECTOR, "[role='navigation']"))
            )
            print("✓ Login Successful!")

        except:
            # Check if there was an error or CAPTCHA
            if "captcha" in driver.page_source.lower() or "verify" in driver.page_source.lower():
                print("⚠ CAPTCHA or verification required. Please complete manually.")
                input("Press Enter after completing CAPTCHA...")
            else:
                print("✗ Login may have failed. Check the browser.")

    except Exception as e:
        print(f"✗ An error occurred: {e}")
        # Take screenshot for debugging
        driver.save_screenshot("login_error.png")
        print("Screenshot saved as 'login_error.png'")

    finally:
        # Keep browser open for a moment to see the result
        print("Script completed. Browser will close in 10 seconds...")
        time.sleep(10)
        driver.quit()


# Security warning
print("⚠ SECURITY WARNING: Avoid hardcoding passwords in scripts!")
print("Consider using environment variables or secure password managers.\n")

# Run the login function
if __name__ == "__main__":
    login_gmail()