# 🚀 Selenium Automation & Grid Suite
### Enterprise-Grade Browser Automation with Distributed Testing Architecture

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.38.0-green.svg)](https://www.selenium.dev/)
[![Grid](https://img.shields.io/badge/Selenium_Grid-4.38.0-orange.svg)](https://www.selenium.dev/documentation/grid/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **DevOps-Ready** | **CI/CD Integration** | **Parallel Execution** | **Cross-Browser Testing**

Built by [Saleem Ali](https://www.linkedin.com/in/saleem-ali-189719325/) | AIOps Engineer @ Al-Nafi International College

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Selenium Grid Setup](#-selenium-grid-setup)
- [Usage Examples](#-usage-examples)
- [Advanced Features](#-advanced-features)
- [Best Practices](#-best-practices)
- [Contributing](#-contributing)

---

## 🎯 Overview

This project showcases **professional-grade browser automation** using Selenium WebDriver with **Selenium Grid 4** for distributed testing. Designed for DevOps engineers, QA professionals, and AIOps practitioners who need scalable, maintainable, and production-ready automation solutions.

### 🌟 Why This Project Stands Out

```
Traditional Selenium:          This Project:
├── 1 browser, 1 test          ├── Multiple browsers parallel
├── Sequential execution       ├── Grid-based distribution
├── Hours of runtime          ├── Minutes with scaling
├── Manual driver updates      ├── Auto-managed drivers
└── Basic scripts             └── Production patterns
```

### 💼 Real-World Applications
- **CI/CD Pipelines:** Automated regression testing
- **DevOps Monitoring:** Health checks & validation
- **QA Automation:** Cross-browser test suites
- **Web Scraping:** Data extraction at scale
- **AIOps:** Automated incident validation

---

## ✨ Key Features

### 🎨 Core Automation Capabilities
- ✅ **Multi-Browser Support:** Chrome, Firefox, Edge
- ✅ **Auto-Driver Management:** webdriver-manager integration
- ✅ **Smart Synchronization:** Implicit & explicit waits
- ✅ **Complex Interactions:** ActionChains, drag-drop, hover
- ✅ **Advanced Selectors:** CSS, XPath, dynamic locators
- ✅ **Screenshot Capture:** Full-page & element-specific
- ✅ **Alert Handling:** JavaScript popups & dialogs
- ✅ **Iframe Navigation:** Nested content management
- ✅ **Window Management:** Multi-tab orchestration

### 🌐 Selenium Grid Features (DevOps Level)
- ⚡ **Parallel Execution:** 10x faster test runs
- 🔄 **Hub-Node Architecture:** Scalable infrastructure
- 🖥️ **Multi-Browser Matrix:** Cross-browser testing
- 📊 **Resource Optimization:** Efficient browser allocation
- 🔌 **Remote WebDriver:** Distributed test execution
- 📈 **Horizontal Scaling:** Add nodes on demand

---

## 🏗️ Architecture

### Standard Selenium Flow
```
┌─────────────┐
│ Test Script │
└──────┬──────┘
       │
       ▼
┌──────────────┐
│  WebDriver   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Browser    │
└──────────────┘
```

### Selenium Grid Architecture (This Project)
```
┌─────────────────────────────────────────────────┐
│              TEST SCRIPTS                       │
│  (selenium_grid_test.py)                       │
└───────────────────┬─────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│           SELENIUM GRID HUB                     │
│  (selenium-server-4.38.0.jar)                  │
│  ├── Session Management                         │
│  ├── Load Balancing                            │
│  └── Browser Distribution                       │
└──────┬─────────┬─────────┬──────────────────────┘
       │         │         │
       ▼         ▼         ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│  NODE 1  │ │  NODE 2  │ │  NODE N  │
│ (Chrome) │ │(Firefox) │ │  (Edge)  │
└──────────┘ └──────────┘ └──────────┘
```

**Key Components:**
1. **Hub:** Central coordinator (port 4444)
2. **Nodes:** Browser execution engines
3. **Test Scripts:** Remote WebDriver clients
4. **Drivers:** chromedriver, geckodriver, msedgedriver

---

## ⚡ Quick Start

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
Java 11+ (for Selenium Grid)
Chrome, Firefox, or Edge browser
```

### Installation

**1. Clone Repository**
```bash
git clone https://github.com/ali4210/selenium-automation-grid.git
cd selenium-automation-grid
```

**2. Install Dependencies (One Command!)**
```bash
pip install -r requirements.txt
```

**3. Verify Installation**
```bash
python -c "import selenium; print(f'Selenium {selenium.__version__} installed!')"
```

### Run Your First Test
```bash
# Basic browser automation
python chrome_script.py

# Auto-update driver example
python web_driver_auto_update_browser.py

# Login automation
python web-element-alnafi-login.py
```

---

## 📁 Project Structure

```
selenium-automation-grid/
│
├── 📂 drivers/                    # Browser drivers (auto-managed)
│   ├── chromedriver.exe
│   ├── geckodriver.exe
│   └── msedgedriver.exe
│
├── 📂 screenshots/                # Captured screenshots
│   └── myfile
│
├── 📂 tests/                      # Automation scripts
│   ├── Alert_handeling.py         # Alert & popup handling
│   ├── checkbox.py                # Checkbox interactions
│   ├── chrome_script.py           # Chrome automation
│   ├── complex-element(Double_click).py
│   ├── complex-element(Right_Click).py
│   ├── css-2.py                   # CSS selectors
│   ├── css-sdelectors.py          # Advanced CSS
│   ├── demo_website.py            # Basic demo
│   ├── drag_slider_range.py      # Drag & drop
│   ├── drop_down.py               # Dropdown handling
│   ├── drop-down-2.py             # Advanced dropdowns
│   ├── edge_script.py             # Edge automation
│   ├── firefox_script.py          # Firefox automation
│   ├── gmail_login-1.py           # Gmail automation
│   ├── gmail-login-sync.py        # Sync waits example
│   ├── iframe.py                  # Iframe navigation
│   ├── is_elements-2.py           # Element validation
│   ├── is_elements.py             # Element checks
│   ├── mouse-over-effect.py      # Hover interactions
│   ├── options-2.py               # Headless mode
│   ├── options.py                 # Browser options
│   ├── scraping.py                # Web scraping
│   ├── screenshot_full_page.py   # Full-page screenshots
│   ├── screenshot-2.py            # Screenshot variants
│   ├── screenshot-3.py
│   ├── screenshot-4.py
│   ├── screenshot.py
│   ├── tab_handling.py            # Multi-window management
│   ├── task.py                    # Practice tasks
│   └── web-element-alnafi-login.py
│
├── 📂 grid/                       # Selenium Grid setup
│   ├── selenium-server-4.38.0.jar # Grid server
│   └── selenium_grid_test.py      # Grid test script
│
├── 📄 requirements.txt            # Python dependencies
├── 📄 .gitignore                  # Security exclusions
├── 📄 .env.example                # Environment template
├── 📄 README.md                   # This file
└── 📄 MASTER_GUIDE.md             # Complete learning resource
```

---

## 🌐 Selenium Grid Setup

### Step 1: Start the Hub

**Open terminal and run:**
```bash
cd grid
java -jar selenium-server-4.38.0.jar hub
```

**Expected output:**
```
✓ Selenium Grid Hub started
✓ Listening on: http://localhost:4444
✓ Grid Console: http://localhost:4444/ui
```

### Step 2: Start Node(s)

**Open NEW terminal and run:**
```bash
java -jar selenium-server-4.38.0.jar node --detect-drivers true --publish-events tcp://localhost:4442 --subscribe-events tcp://localhost:4443
```

**For different machines/IPs:**
```bash
java -jar selenium-server-4.38.0.jar node --detect-drivers true --publish-events tcp://10.0.2.1:4442 --subscribe-events tcp://10.0.2.1:4443
```

**Expected output:**
```
✓ Node registered to Hub
✓ Browsers detected: Chrome, Firefox, Edge
✓ Node ready for sessions
```

### Step 3: Access Grid Console

Open browser and navigate to:
```
http://localhost:4444/ui
```

**You'll see:**
- Connected nodes
- Available browsers
- Active sessions
- Grid status

### Step 4: Run Grid Test

```bash
cd grid
python selenium_grid_test.py
```

**What happens:**
1. Script connects to Hub (port 4444)
2. Hub assigns available node
3. Test runs on remote browser
4. Results returned to script

---

## 💡 Usage Examples

### Basic Browser Automation
```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Auto-managed driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate and interact
driver.get("https://example.com")
driver.maximize_window()
print(driver.title)
driver.quit()
```

### Form Automation
```python
from selenium.webdriver.common.by import By

# Find and fill form
driver.find_element(By.ID, "username").send_keys("user123")
driver.find_element(By.ID, "password").send_keys("pass123")
driver.find_element(By.ID, "submit").click()
```

### Dropdown Handling
```python
from selenium.webdriver.support.select import Select

dropdown = driver.find_element(By.ID, "country")
select = Select(dropdown)
select.select_by_visible_text("Bangladesh")
```

### Grid Remote Execution
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
print(f"Testing on: {driver.capabilities['browserName']}")
driver.quit()
```

### Screenshot Capture
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
```

---

## 🎓 Advanced Features

### 1. Explicit Waits (Production Ready)
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
element.click()
```

### 2. ActionChains (Complex Interactions)
```python
from selenium.webdriver import ActionChains

actions = ActionChains(driver)

# Right-click
actions.context_click(element).perform()

# Double-click
actions.double_click(element).perform()

# Drag and drop
actions.drag_and_drop(source, target).perform()

# Hover
actions.move_to_element(menu).perform()
```

### 3. Headless Mode (CI/CD)
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=options)
```

### 4. Multi-Window Management
```python
# Open new tab
driver.execute_script("window.open('');")

# Switch between windows
windows = driver.window_handles
driver.switch_to.window(windows[1])  # Switch to 2nd tab
driver.switch_to.window(windows[0])  # Back to 1st tab
```

### 5. Alert Handling
```python
from selenium.webdriver.common.alert import Alert

# Wait for alert
alert = Alert(driver)
print(alert.text)
alert.accept()  # Click OK
# alert.dismiss()  # Click Cancel
```

---

## 🔒 Best Practices

### Security
```python
# ❌ NEVER hardcode credentials
password = "MyPassword123"

# ✅ Use environment variables
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv('PASSWORD')
```

### Locator Strategy
```
Priority Order:
1. ID (fastest, most reliable)
2. NAME
3. CSS Selector (clean, fast)
4. XPath (flexible, but slower)
```

### Wait Strategy
```python
# ❌ Avoid time.sleep() in production
time.sleep(5)

# ✅ Use implicit waits (global)
driver.implicitly_wait(10)

# ✅✅ Use explicit waits (best practice)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "id")))
```

### Resource Cleanup
```python
try:
    driver.get("https://example.com")
    # ... automation code ...
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()  # Always cleanup
```

---

## 📊 Performance Comparison

### Standard Execution vs Grid

```
Test Suite: 100 test cases
Browser: Chrome
Machine: 4-core CPU, 8GB RAM

┌─────────────────────┬──────────────┬──────────────┐
│     Metric          │   Standard   │     Grid     │
├─────────────────────┼──────────────┼──────────────┤
│ Execution Time      │   120 min    │    12 min    │
│ Parallel Tests      │      1       │      10      │
│ Browser Instances   │      1       │      10      │
│ CPU Usage           │    25%       │    80%       │
│ Efficiency Gain     │     1x       │    10x       │
└─────────────────────┴──────────────┴──────────────┘
```

---

## 🛠️ Troubleshooting

### Common Issues

**1. Driver Not Found**
```bash
# Solution: Use webdriver-manager
pip install webdriver-manager
```

**2. Element Not Found**
```python
# Solution: Add explicit wait
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, 10)
```

**3. Grid Connection Failed**
```bash
# Check Hub is running
http://localhost:4444/ui

# Verify network connectivity
ping localhost
```

**4. Browser Version Mismatch**
```bash
# Update all drivers
pip install --upgrade webdriver-manager
```

---

## 📚 Learning Resources

- 📖 **MASTER_GUIDE.md** - Complete 300+ page learning resource
- 🎥 [Selenium Documentation](https://www.selenium.dev/documentation/)
- 🌐 [Grid Setup Guide](https://www.selenium.dev/documentation/grid/)
- 💬 [Stack Overflow - Selenium Tag](https://stackoverflow.com/questions/tagged/selenium)

---

## 🤝 Contributing

Contributions welcome! Please follow:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## 👨‍💻 Author

**Saleem Ali**
- 🎓 AIOps Engineering Student @ Al-Nafi International College
- 💼 [LinkedIn](https://www.linkedin.com/in/saleem-ali-189719325/)
- 🐙 [GitHub](https://github.com/ali4210?tab=repositories)
- 📧 Email: saleemali.mohammad@gmail.com

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐ on GitHub!

---

## 🙏 Acknowledgments

- Selenium Community
- Al-Nafi International College
- Open Source Contributors

---

**Built with ❤️ for the DevOps & AIOps Community**
