 FakerX Selenium Automation Project 🚀

An end-to-end web automation project built with Python, Selenium WebDriver,
and BeautifulSoup.

This project was created to practice real-world browser automation,
DOM interaction, explicit waits, element handling, debugging, and
end-to-end workflow automation.

---

## 🎯 Project Objective

The objective of this project is to automate a complete shopping workflow
on the Sauce Demo Shopify website.

The automation starts from the homepage, searches for a product, opens the
product page, adds the product to the cart, verifies the cart, proceeds to
checkout, fills the checkout form, and verifies the final result.

---

## 🌐 Target Website

Sauce Demo Shopify

https://sauce-demo.myshopify.com/

> This project is intended for learning and automation practice.

---

## 🔄 Automation Workflow

The complete workflow is:

```text
Open Website
      ↓
Find Search Box
      ↓
Search for "jacket"
      ↓
Find Grey jacket
      ↓
Open Product Page
      ↓
Verify Product Name
      ↓
Verify Product Price
      ↓
Add Product to Cart
      ↓
Open Cart
      ↓
Verify Product in Cart
      ↓
Verify Cart Price
      ↓
Verify Quantity
      ↓
Open Checkout
      ↓
Fill Checkout Information
      ↓
Find Pay Now Button
      ↓
Click Pay Now
      ↓
Verify Final Result
      ↓
Save Screenshot
      ↓
Project Completed
🛠️ Technologies Used
Python
Selenium WebDriver
BeautifulSoup4
Google Chrome
Chrome WebDriver
HTML / DOM
CSS Selectors
📚 Selenium Concepts Practiced

This project covers several important Selenium concepts:

WebDriver
Chrome WebDriver
driver.get()
driver.current_url
driver.title
driver.page_source
find_element()
find_elements()
By.ID
By.NAME
By.CSS_SELECTOR
WebElement
click()
send_keys()
clear()
WebDriverWait
Expected Conditions
presence_of_element_located()
visibility_of_element_located()
element_to_be_clickable()
Explicit waits
Browser navigation
DOM inspection
Screenshot capture
Exception handling
Stale element handling
Timeout debugging
🔎 Locators Used

The project demonstrates different ways of locating HTML elements.

Examples include:

By.ID
By.NAME
By.CSS_SELECTOR

For example:

(By.ID, "product-1")
(By.NAME, "updates[]")
(By.CSS_SELECTOR, 'input[name="q"]')
(By.CSS_SELECTOR, 'h1[itemprop="name"]')

The locators were selected by inspecting the actual HTML/DOM of the
target website.

⏳ Explicit Waits

The project uses Selenium's WebDriverWait instead of relying only on
fixed delays.

Example:

wait = WebDriverWait(driver, 10)

Then:

wait.until(
    EC.element_to_be_clickable(
        (By.ID, "checkout")
    )
)

This allows Selenium to wait for the required browser state before
continuing.

🧠 DOM Investigation

BeautifulSoup was also used to inspect the HTML returned by Selenium.

Example:

soup = BeautifulSoup(
    driver.page_source,
    "html.parser"
)

This was especially useful during cart debugging.

The project used DOM inspection to determine whether the product was
actually present in the cart instead of assuming that the cart operation
had succeeded.

🐛 Debugging Experience

A major part of this project was debugging real Selenium failures.

StaleElementReferenceException

A stale element occurred when Selenium located an element and the page
subsequently replaced the DOM element.

Conceptually:

Selenium finds element
       ↓
Page changes
       ↓
Original DOM element is replaced
       ↓
Old WebElement reference becomes invalid
       ↓
StaleElementReferenceException

The solution was to locate a fresh element immediately before interacting
with it.

TimeoutException

Timeouts occurred when Selenium waited for an element or state that did
not appear within the configured timeout.

Instead of immediately changing the locator, the page was investigated
to determine what actually existed in the DOM.

This helped identify incorrect assumptions about the cart structure and
element attributes.

🛒 Cart Verification

The project verifies that the product was successfully added to the cart.

It checks:

Product name
Product URL
Product price
Quantity
Cart section

Example HTML discovered during the project:

<input
    id="updates_611945025"
    name="updates[]"
    type="text"
    value="1"
>

This HTML inspection was used to determine the correct Selenium locator
for the quantity field.

💳 Checkout Automation

After verifying the cart, Selenium opens the checkout page and fills
the checkout form.

The automation handles fields such as:

Email
First name
Last name
Company
Address
Address 2
Postal code
Phone
City

The project then locates the Pay Now button and verifies that the
button is displayed and enabled.

✅ Final Verification

After clicking Pay Now, the script performs final verification.

It checks:

driver.current_url
driver.title

and searches the page source for relevant final-result content.

The project also saves a screenshot after reaching the final stage.

📸 Screenshot

A screenshot is generated after the final verification stage.

Example:

checkout_payment_stage.png

This provides a visual record that the automation reached the expected
final stage.

📁 Project Structure
FakerX-Selenium-Automation/
│
├── main.py
├── requirements.txt
├── README.md
├── screenshots/
│   └── checkout_payment_stage.png
└── .gitignore
⚙️ Requirements

The project requires:

Python 3
Google Chrome
Selenium
BeautifulSoup4

Python packages are listed in:

requirements.txt

Contents:

selenium>=4.0
beautifulsoup4>=4.0
🚀 Installation
1. Clone the repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
2. Enter the project directory
cd FakerX-Selenium-Automation
3. Install dependencies
pip install -r requirements.txt
4. Run the project
python main.py
🌐 Browser

The project uses Google Chrome through Selenium WebDriver.

The browser is started with:

driver = webdriver.Chrome()

Selenium Manager can automatically manage the required driver in modern
Selenium versions.

🧪 What This Project Demonstrates

This project demonstrates the ability to:

Automate a real browser workflow
Interact with HTML elements
Build Selenium locators
Use explicit waits
Work with dynamically changing DOM elements
Diagnose Selenium exceptions
Inspect HTML when automation fails
Verify application state
Automate forms
Perform end-to-end browser testing
Capture automation evidence with screenshots
📈 Learning Outcome

The main lesson from this project was that browser automation is not
simply a sequence of click() commands.

A reliable Selenium automation script must understand:

DOM
 ↓
Element locator
 ↓
Element state
 ↓
Browser/page changes
 ↓
Synchronization
 ↓
Interaction
 ↓
Verification

When automation fails, inspecting the actual browser state and DOM is
more reliable than randomly changing waits or locators.

🔮 Future Improvements

Possible future improvements include:

Page Object Model
Reusable helper functions
Better test organization
More test cases
Parameterized product searches
Better reporting
Logging
Automated screenshots on failure
CI/CD integration
Pytest integration

These improvements are intentionally outside the scope of this first
project.

⚠️ Disclaimer

This project is an educational Selenium automation project.

It is designed for learning browser automation, web testing, DOM
inspection, synchronization, and debugging.

Do not use automation against websites without appropriate authorization.

👨‍💻 Author

Mr Faker

Python Automation & Cyber Security Learner

📌 Project Status

Completed ✅

The complete end-to-end automation workflow has been successfully tested:

Search
  ↓
Product
  ↓
Cart
  ↓
Checkout
  ↓
Form
  ↓
Pay Now
  ↓
Final Verification
  ↓
Screenshot
  ↓
SUCCESS ✅
