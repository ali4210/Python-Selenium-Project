
# Alnafi Selenium & Scraping Portfolio: The Complete Framework
**Author:** Saleem Ali
**Focus:** Web Automation, QA Testing, Stealth Bots, & Data Extraction
**Tech Stack:** Python 3.x, Selenium WebDriver, BeautifulSoup4, ActionChains, Pytest

---

## ==>> 1. Comprehensive File Index (File-to-Concept Map)
*This table maps every file in your project to the skill it demonstrates.*

| Category | File Name | Skill Demonstrated |
| :--- | :--- | :--- |
| **Setup** | `web_driver_auto_update...` | Auto-installing Drivers (Manager) |
| | `chrome_script.py` | Basic Chrome Initialization |
| | `edge_script.py` / `edge-normal` | Edge Browser Setup |
| | `firefox_script.py` | Firefox (Gecko) Setup |
| | `options.py` / `options-2.py` | **Headless Mode** (Invisible execution) |
| **Locators** | `css-sdelectors.py` / `css-2.py` | Advanced CSS (Attributes & IDs) |
| | `is_elements.py` / `is_elements-2` | Boolean logic to check element existence |
| | `web-element-alnafi-login.py` | Basic ID/Name locators |
| **Controls** | `checkbox.py` | Looping through checkbox lists |
| | `drop_down.py` / `drop-down-2.py` | Handling `<select>` and `<option>` tags |
| | `task.py` | Extracting attributes (lang) from options |
| **Actions** | `drag_slider_range.py` | Drag-and-Drop offsets |
| | `mouse-over-effect.py` | Hover effects (Menus) |
| | `complex-element(Double_click)` | ActionChains: Double Click |
| | `complex-element(Right_Click)` | ActionChains: Context Click |
| **Windows** | `iframe.py` | Switching context to iFrames |
| | `tab_handling.py` | Managing multiple Browser Tabs |
| | `Alert_handeling.py` | Accepting/Dismissing JS Alerts |
| **Stealth** | `gmail_login-1.py` | **Human Emulation** (Random delays/mouse) |
| | `gmail-login-sync.py` | Explicit Waits (`WebDriverWait`) |
| **Data** | `scraping.py` | **BeautifulSoup** (HTML Parsing) |
| | `screenshot.py` - `screenshot-4.py` | Capturing Evidence (PNG) |
| | `screenshot_full_page.py` | Javascript scrolling for full capture |

---

## ==>> Module 1: Driver Architecture & Options

### => Auto-Update & Headless Mode
* **Files:** `web_driver_auto_update_browser.py`, `options.py`
* **Concept:** Decouple code from local driver paths. Use `webdriver_manager`.
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Headless Setup (Runs in background)
chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

```

---

## ==>> Module 2: Advanced Locators & Controls

### => Dynamic Checkbox Handling

* **File:** `checkbox.py`
* **Concept:** Iterate through a list of elements to interact with them securely.

```python
# Click all checkboxes with a specific class
checkboxes = driver.find_elements(By.CLASS_NAME, 'checkboxGroups')
for box in checkboxes:
    if not box.isSelected():
        box.click()

```

### => CSS Selectors

* **File:** `css-sdelectors.py`
* **Concept:** Use CSS for elements with dynamic IDs.

```python
# Target input by attribute
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("user@test.com")

```

---

## ==>> Module 3: Complex Mouse Actions (ActionChains)

### => Double & Right Click

* **Files:** `complex-element(Double_click).py`, `complex-element(Right_Click).py`
* **Concept:** Using `ActionChains` for interactions that standard `.click()` cannot do.

```python
from selenium.webdriver import ActionChains

element = driver.find_element(By.ID, "clickable-box")
actions = ActionChains(driver)

# Right Click (Context Click)
actions.context_click(element).perform()

# Double Click
actions.double_click(element).perform()

```

### => Drag and Drop Slider

* **File:** `drag_slider_range.py`

```python
slider = driver.find_element(By.XPATH, '//*[@id="slider"]')
# Move slider 50px to the left
actions.drag_and_drop_by_offset(slider, -50, 0).perform()

```

---

## ==>> Module 4: Window & Frame Management

### => Handling iFrames

* **File:** `iframe.py`
* **Concept:** You cannot interact with elements inside an `<iframe>` until you switch context.

```python
driver.switch_to.frame("moneyiframe")
# Now you can interact with elements inside the frame
print(driver.find_element(By.ID, "nseindex").text)
driver.switch_to.default_content() # Return to main page

```

### => Multi-Tab Handling

* **File:** `tab_handling.py`

```python
# Switch to new tab
driver.switch_to.window(driver.window_handles[1])

```

---

## ==>> Module 5: Stealth & Human Simulation

### => The "Stealth" Login Algorithm

* **File:** `gmail_login-1.py`
* **Concept:** Bypassing bot detection by randomizing typing speed and mouse movements.

```python
import random, time

def human_type(element, text):
    for char in text:
        element.send_keys(char)
        # Random delay between 0.05s and 0.2s mimics human fingers
        time.sleep(random.uniform(0.05, 0.2))

# Disable Automation Flags
options.add_argument("--disable-blink-features=AutomationControlled")

```

---

## ==>> Module 6: Web Scraping (BeautifulSoup)

### => Static Data Extraction

* **File:** `scraping.py`
* **Concept:** Unlike Selenium, `BeautifulSoup` parses static HTML efficiently without opening a browser.

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("[https://example.com](https://example.com)")
soup = BeautifulSoup(response.text, 'html.parser')

# Extract Page Title
print(f"Page Title: {soup.title.string}")

# Extract all Links
for link in soup.find_all('a'):
    print(link.get('href'))

```

---

## ==>> Module 7: Evidence Collection

### => Full Page & Element Screenshots

* **Files:** `screenshot_full_page.py`, `screenshot.py`
* **Concept:** Capture specific elements or the entire DOM height using JS.

```python
# 1. Element Screenshot
driver.find_element(By.ID, "login-btn").screenshot("btn_evidence.png")

# 2. Full Page (via Javascript)
width = driver.execute_script("return document.body.scrollWidth")
height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(width, height)
driver.save_screenshot("full_page.png")

```

---

**Status:** Completed
**Skills:** Browser Automation, Human Emulation (Stealth), Data Extraction (BS4), QA Testing.

```

```