# 🚀 SELENIUM & GRID QUICK REFERENCE CARD
### Your Essential Commands & Patterns Cheat Sheet

---

## ⚡ INSTALLATION & SETUP

### Install Dependencies
```bash
# All at once
pip install -r requirements.txt

# Individual packages
pip install selenium==4.38.0
pip install webdriver-manager==4.0.1
pip install beautifulsoup4==4.12.2
```

### Verify Installation
```bash
python -c "import selenium; print(selenium.__version__)"
```

---

## 🌐 WEBDRIVER BASICS

### Chrome (Auto-Update)
```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://example.com")
driver.quit()
```

### Firefox
```python
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
```

### Edge
```python
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
```

---

## 🎯 LOCATORS

### Import
```python
from selenium.webdriver.common.by import By
```

### The 8 Locators
```python
# 1. ID (Fastest)
driver.find_element(By.ID, "username")

# 2. NAME
driver.find_element(By.NAME, "email")

# 3. CLASS_NAME
driver.find_element(By.CLASS_NAME, "btn-login")

# 4. TAG_NAME
driver.find_element(By.TAG_NAME, "input")

# 5. LINK_TEXT
driver.find_element(By.LINK_TEXT, "Sign Up")

# 6. PARTIAL_LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")

# 7. CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "input[name='email']")

# 8. XPATH
driver.find_element(By.XPATH, "//input[@name='email']")
```

---

## 📝 CSS SELECTORS

```css
#id                    /* By ID */
.class                 /* By class */
tag                    /* By tag */
[attribute='value']    /* By attribute */
tag#id                 /* Combined */
tag.class              /* Combined */
tag[attr='val']        /* Combined */
parent > child         /* Direct child */
ancestor descendant    /* Any descendant */
element:first-child    /* First child */
element:nth-child(n)   /* Nth child */
```

### Examples
```python
By.CSS_SELECTOR, "#username"
By.CSS_SELECTOR, "input.form-control"
By.CSS_SELECTOR, "input[type='email']"
By.CSS_SELECTOR, "form > input"
```

---

## 🔍 XPATH

### Basic XPath
```xpath
//tag[@attribute='value']
//input[@id='username']
//button[@type='submit']
```

### Advanced XPath
```xpath
//button[text()='Login']              # Exact text
//button[contains(text(), 'Log')]     # Partial text
//input[@id='x' and @type='text']     # Multiple conditions
//div[@class='form']//input           # Descendant
//input[@id='email']/parent::div      # Parent
//input[@id='email']/following-sibling::button  # Sibling
```

---

## 🖱️ ELEMENT INTERACTIONS

### Basic Actions
```python
# Find element
element = driver.find_element(By.ID, "username")

# Type text
element.send_keys("myusername")

# Click
element.click()

# Clear
element.clear()

# Get text
text = element.text

# Get attribute
value = element.get_attribute("value")

# Check if displayed
is_visible = element.is_displayed()

# Check if enabled
is_enabled = element.is_enabled()

# Check if selected (checkbox/radio)
is_selected = element.is_selected()
```

---

## 📋 DROPDOWNS

```python
from selenium.webdriver.support.select import Select

dropdown = driver.find_element(By.ID, "country")
select = Select(dropdown)

# Select by visible text (most common)
select.select_by_visible_text("Bangladesh")

# Select by value
select.select_by_value("bd")

# Select by index
select.select_by_index(2)

# Get selected option
selected = select.first_selected_option
print(selected.text)

# Get all options
for option in select.options:
    print(option.text)
```

---

## ⏰ WAITS

### Implicit Wait (Global)
```python
driver.implicitly_wait(10)  # Wait up to 10 seconds
```

### Explicit Wait (Specific)
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

# Wait for element to be clickable
element = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)

# Wait for element to be present
element = wait.until(
    EC.presence_of_element_located((By.ID, "result"))
)

# Wait for element to be visible
element = wait.until(
    EC.visibility_of_element_located((By.ID, "message"))
)
```

### Common Expected Conditions
```python
EC.presence_of_element_located()
EC.visibility_of_element_located()
EC.element_to_be_clickable()
EC.title_is("Expected Title")
EC.title_contains("Partial")
EC.url_contains("example.com")
EC.alert_is_present()
EC.text_to_be_present_in_element()
```

---

## 🖱️ ACTIONCHAINS

```python
from selenium.webdriver import ActionChains

actions = ActionChains(driver)

# Right-click
actions.context_click(element).perform()

# Double-click
actions.double_click(element).perform()

# Hover
actions.move_to_element(element).perform()

# Drag and drop
actions.drag_and_drop(source, target).perform()

# Drag by offset
actions.drag_and_drop_by_offset(element, 50, 0).perform()

# Click and hold
actions.click_and_hold(element).perform()

# Release
actions.release().perform()

# Chain multiple actions
actions.move_to_element(menu).click(submenu).perform()
```

---

## ⚠️ ALERTS

```python
from selenium.webdriver.common.alert import Alert

# Get alert
alert = Alert(driver)

# Get alert text
print(alert.text)

# Accept (OK button)
alert.accept()

# Dismiss (Cancel button)
alert.dismiss()

# Send text (for prompt)
alert.send_keys("My input")
```

---

## 🖼️ IFRAMES

```python
# Switch to iframe by index
driver.switch_to.frame(0)

# Switch to iframe by name or ID
driver.switch_to.frame("frameName")

# Switch to iframe by element
iframe = driver.find_element(By.ID, "myframe")
driver.switch_to.frame(iframe)

# Switch back to main content
driver.switch_to.default_content()

# Switch to parent frame
driver.switch_to.parent_frame()
```

---

## 🪟 WINDOWS & TABS

```python
# Get all window handles
windows = driver.window_handles

# Switch to window by index
driver.switch_to.window(windows[1])

# Switch back to first window
driver.switch_to.window(windows[0])

# Open new tab (JavaScript)
driver.execute_script("window.open('');")

# Close current window
driver.close()

# Quit all windows
driver.quit()
```

---

## 📸 SCREENSHOTS

```python
# Full page screenshot
driver.save_screenshot("page.png")

# Element screenshot
element = driver.find_element(By.ID, "logo")
element.screenshot("logo.png")

# Full-page scroll capture
total_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(1920, total_height)
driver.save_screenshot("fullpage.png")

# Screenshot with timestamp
import time
filename = f"screenshot_{time.time()}.png"
driver.save_screenshot(filename)
```

---

## 🎨 BROWSER OPTIONS

### Chrome Headless
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=service, options=options)
```

### Firefox Headless
```python
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(service=service, options=options)
```

### Other Useful Options
```python
options.add_argument("--start-maximized")
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
options.add_argument("user-agent=Mozilla/5.0...")
```

---

## 🌐 SELENIUM GRID COMMANDS

### Start Hub
```bash
java -jar selenium-server-4.38.0.jar hub
```

### Start Node (Local)
```bash
java -jar selenium-server-4.38.0.jar node --detect-drivers true --publish-events tcp://localhost:4442 --subscribe-events tcp://localhost:4443
```

### Start Node (Remote)
```bash
java -jar selenium-server-4.38.0.jar node --detect-drivers true --publish-events tcp://10.0.2.1:4442 --subscribe-events tcp://10.0.2.1:4443
```

### Grid Console
```
http://localhost:4444/ui
```

---

## 🔌 REMOTE WEBDRIVER (Grid)

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

hub_url = "http://localhost:4444/wd/hub"
chrome_options = ChromeOptions()

driver = webdriver.Remote(
    command_executor=hub_url,
    options=chrome_options
)

driver.get("https://example.com")
print(f"Browser: {driver.capabilities['browserName']}")
driver.quit()
```

---

## 🔧 USEFUL BROWSER COMMANDS

```python
# Navigate
driver.get("https://example.com")
driver.back()
driver.forward()
driver.refresh()

# Window management
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window()
driver.set_window_size(1920, 1080)

# Get info
title = driver.title
url = driver.current_url
page_source = driver.page_source

# Execute JavaScript
driver.execute_script("return document.title")
driver.execute_script("arguments[0].click();", element)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Cookies
driver.get_cookies()
driver.get_cookie("session_id")
driver.add_cookie({'name': 'key', 'value': 'value'})
driver.delete_cookie("session_id")
driver.delete_all_cookies()
```

---

## 🛠️ TROUBLESHOOTING

### Element Not Found
```python
# Use explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "myid")))
```

### Element Not Clickable
```python
# Scroll into view
driver.execute_script("arguments[0].scrollIntoView();", element)

# Use JavaScript click
driver.execute_script("arguments[0].click();", element)

# Use ActionChains
from selenium.webdriver import ActionChains
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
```

### Stale Element
```python
# Re-find element
try:
    element.click()
except StaleElementReferenceException:
    element = driver.find_element(By.ID, "myid")
    element.click()
```

---

## 🔒 SECURITY BEST PRACTICES

### Use Environment Variables
```python
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
```

### .env File
```
USERNAME=myuser
PASSWORD=mypass123
API_KEY=xyz123
```

### Never Commit
```bash
# Add to .gitignore
.env
*password*
*credentials*
```

---

## 📊 COMMON PATTERNS

### Login Flow
```python
driver.get("https://example.com/login")
driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("pass")
driver.find_element(By.ID, "submit").click()
```

### Check Element Exists
```python
def is_element_present(locator_type, locator_value):
    elements = driver.find_elements(locator_type, locator_value)
    return len(elements) > 0
```

### Wait for Page Load
```python
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
```

### Handle Dynamic Content
```python
wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.visibility_of_element_located((By.ID, "dynamic-content"))
)
```

---

## 🎯 KEYBOARD SHORTCUTS

```python
from selenium.webdriver.common.keys import Keys

# Special keys
element.send_keys(Keys.ENTER)
element.send_keys(Keys.TAB)
element.send_keys(Keys.ESCAPE)
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.DELETE)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ARROW_UP)

# Combinations
element.send_keys(Keys.CONTROL, 'a')  # Ctrl+A
element.send_keys(Keys.CONTROL, 'c')  # Ctrl+C
element.send_keys(Keys.CONTROL, 'v')  # Ctrl+V
```

---

## 📚 QUICK TIPS

✅ **Always use explicit waits** instead of time.sleep()
✅ **Prefer CSS Selectors** over XPath (faster)
✅ **Use ID locators** when available (most reliable)
✅ **Maximize window** for consistent behavior
✅ **Handle exceptions** with try-except-finally
✅ **Close/quit driver** in finally block
✅ **Never hardcode passwords** - use environment variables
✅ **Add implicit wait** at driver initialization
✅ **Use relative locators** over absolute XPaths
✅ **Test in headless mode** for CI/CD

---

## 🚀 PERFORMANCE OPTIMIZATION

```python
# Implicit wait (set once)
driver.implicitly_wait(10)

# Page load timeout
driver.set_page_load_timeout(30)

# Script timeout
driver.set_script_timeout(20)

# Headless mode (faster)
options.add_argument("--headless")

# Disable images (faster loading)
options.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.images": 2}
)
```

---

## 📞 HELPFUL RESOURCES

- 🌐 **Selenium Docs:** https://www.selenium.dev/documentation/
- 📖 **Grid Guide:** https://www.selenium.dev/documentation/grid/
- 💬 **Stack Overflow:** https://stackoverflow.com/questions/tagged/selenium
- 📚 **Your Master Guide:** MASTER_GUIDE.md

---

**💡 Pro Tip:** Keep this reference handy while coding. Print it or save as PDF!

**👨‍💻 Author:** Saleem Ali | AIOps Engineer
**📅 Last Updated:** December 2024
**🔗 GitHub:** https://github.com/ali4210
