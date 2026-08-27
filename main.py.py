print("=== FAKERX SELENIUM PROJECT START ===")

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    WebDriverException
)

from bs4 import BeautifulSoup


# ============================================================
# CONFIGURATION
# ============================================================

URL = "https://sauce-demo.myshopify.com/"
WAIT_TIME = 10

SEARCH_TERM = "jacket"

EMAIL = "test@example.com"
FIRST_NAME = "haseeb"
LAST_NAME = "khan"
COMPANY = "FAKER_X"
ADDRESS = "Rashakai"
ADDRESS2 = "House1"
POSTAL_CODE = "House1234"
PHONE = "03299302724"
CITY = "mardan"


# ============================================================
# DRIVER SETUP
# ============================================================

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, WAIT_TIME)


try:

    # ========================================================
    # 1. OPEN WEBSITE
    # ========================================================

    print("\n[1] Opening website...")

    driver.get(URL)

    print("[OK] Website opened")
    print("[INFO] Title:", driver.title)
    print("[INFO] URL:", driver.current_url)


    # ========================================================
    # 2. SEARCH FOR JACKET
    # ========================================================

    print("\n[2] Searching for:", SEARCH_TERM)

    search_box = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[name="q"]')
        )
    )

    search_box.clear()
    search_box.send_keys(SEARCH_TERM)
    search_box.send_keys(Keys.ENTER)

    print("[OK] Search submitted")


    # ========================================================
    # 3. WAIT FOR SEARCH RESULT
    # ========================================================

    print("\n[3] Waiting for Grey jacket...")

    wait.until(
        EC.presence_of_element_located(
            (By.ID, "product-1")
        )
    )

    print("[OK] Grey jacket found")


    # ========================================================
    # 4. GET FRESH JACKET ELEMENT
    # ========================================================
    #
    # IMPORTANT:
    # We locate the element again immediately before clicking.
    # This avoids stale-element problems after page changes.
    # ========================================================

    print("\n[4] Getting fresh jacket element...")

    def click_jacket(driver):

        try:
            jacket = driver.find_element(
                By.ID,
            "product-1"
            )

            print("[DEBUG] Fresh jacket element found")

            jacket.click()

            print("[DEBUG] Jacket click succeeded")

            return True

        except StaleElementReferenceException:
            print("[DEBUG] Jacket became stale. Selenium will retry...")
            return False


    wait.until(click_jacket)

    print("[OK] Jacket clicked successfully")

    # ========================================================
    # 5. PRODUCT PAGE
    # ========================================================

    print("\n[5] Checking product page...")

    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'h1[itemprop="name"]')
        )
    )

    product_price = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "span.product-price")
        )
    )

    print("[OK] Product page loaded")

    print("Product name:", product_name.text)
    print("Product price:", product_price.text)
    print("Product URL:", driver.current_url)
    print("Page title:", driver.title)


    # ========================================================
    # 6. PRICE INVESTIGATION
    # ========================================================

    print("\n[6] Checking price elements...")

    prices = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "span.product-price")
        )
    )

    print("[OK] Number of prices found:", len(prices))

    print(
        "[INFO] itemprop='price' in source:",
        'itemprop="price"' in driver.page_source
    )

    print(
        "[INFO] product-price in source:",
        "product-price" in driver.page_source
    )


    # ========================================================
    # 7. ADD TO CART
    # ========================================================

    print("\n[7] Adding product to cart...")

    add_to_cart = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add")
        )
    )

    print("[OK] Add to Cart button found")

    add_to_cart.click()

    print("[OK] Add to Cart clicked")

    time.sleep(5)


    # ========================================================
    # 8. OPEN CART DIRECTLY
    # ========================================================
    #
    # The site does NOT necessarily navigate to /cart after
    # clicking Add to Cart.
    #
    # Therefore we explicitly navigate to the cart.
    # ========================================================

    print("\n[8] Opening cart...")

    driver.get(URL + "cart")

    print("[OK] Cart URL requested")
    print("[INFO] Current URL:", driver.current_url)


    # ========================================================
    # 9. WAIT FOR CART PAGE
    # ========================================================

    print("\n[9] Waiting for cart page...")

    cart = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "cart")
        )
    )

    print("[OK] Cart section found")


    # ========================================================
    # 10. VERIFY PRODUCT IN CART
    # ========================================================

    # ========================================================
# 10. VERIFY PRODUCT IN CART
# ========================================================

    print("\n[10] Inspecting products actually present in cart...")

# Get all links inside the cart
    cart_links = driver.find_elements(
        By.CSS_SELECTOR,
        "#cart a"
    )

    print("[DEBUG] Number of links inside cart:", len(cart_links))

    for link in cart_links:

        try:
            print(
                "[DEBUG] LINK TEXT:",
                repr(link.text),
                "| HREF:",
                link.get_attribute("href")
            )

        except StaleElementReferenceException:
            print("[DEBUG] A cart link became stale")


# --------------------------------------------------------
# BeautifulSoup inspection
# --------------------------------------------------------

    soup = BeautifulSoup(
        driver.page_source,
        "html.parser"
    )

    cart_bs = soup.find(
        "section",
        id="cart"
    )

    print("\n[DEBUG] CART HTML:")
    print(cart_bs)


# --------------------------------------------------------
# Search for Grey jacket using text
# --------------------------------------------------------

    print("\n[10B] Searching for Grey jacket by text...")

    cart_product = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//section[@id='cart']//a[contains(., 'Grey jacket')]"
            )
        )   
    )

    print("[OK] Product found in cart")
    print("Cart product:", cart_product.text)
    print("Cart product href:", cart_product.get_attribute("href"))

    # ========================================================
    # 11. VERIFY CART PRICE
    # ========================================================
    #
    # IMPORTANT:
    # "#cart .price.desktop" can match the "Price" header.
    #
    # We specifically target the cart row.
    # ========================================================

    print("\n[11] Verifying cart price...")

    cart_price = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#cart .row .price.desktop"
            )
        )
    )

    print("[OK] Cart product price found")
    print("Cart price:", cart_price.text)


    # ========================================================
    # 12. VERIFY QUANTITY
    # ========================================================

    print("\n[12] Verifying quantity...")

    cart_quantity = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#cart input[name="updates[]"]')
        )
    )

    print(
        "[OK] Cart quantity:",
        cart_quantity.get_attribute("value")
    )

    # ========================================================
    # 13. BEAUTIFULSOUP CART CHECK
    # ========================================================

    print("\n[13] Running BeautifulSoup verification...")

    soup = BeautifulSoup(
        driver.page_source,
        "html.parser"
    )

    cart_bs = soup.find(
        "section",
        id="cart"
    )

    if cart_bs:
        print("[OK] BeautifulSoup found cart section")
    else:
        print("[WARNING] BeautifulSoup could not find cart")


    # ========================================================
    # 14. CHECKOUT
    # ========================================================

    print("\n[14] Opening checkout...")

    checkout = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    )

    print("[OK] Checkout button found")
    print("[INFO] Checkout HTML:")
    print(checkout.get_attribute("outerHTML"))

    checkout.click()

    print("[OK] Checkout clicked")


    # ========================================================
    # 15. WAIT FOR CHECKOUT PAGE
    # ========================================================

    print("\n[15] Waiting for checkout page...")

    email = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "email")
        )
    )

    print("[OK] Checkout page loaded")
    print("[INFO] Checkout URL:", driver.current_url)


    # ========================================================
    # 16. FILL EMAIL
    # ========================================================

    print("\n[16] Filling email...")

    email.send_keys(EMAIL)

    print("[OK] Email entered")


    # ========================================================
    # 17. FIRST NAME
    # ========================================================

    print("\n[17] Filling first name...")

    firstname = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "firstName")
        )
    )

    firstname.send_keys(FIRST_NAME)

    print("[OK] First name entered")


    # ========================================================
    # 18. LAST NAME
    # ========================================================

    print("\n[18] Filling last name...")

    last_name = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "lastName")
        )
    )

    last_name.send_keys(LAST_NAME)

    print("[OK] Last name entered")


    # ========================================================
    # 19. COMPANY
    # ========================================================

    print("\n[19] Filling company...")

    company = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "company")
        )
    )

    company.send_keys(COMPANY)

    print("[OK] Company entered")


    # ========================================================
    # 20. ADDRESS
    # ========================================================

    print("\n[20] Filling address...")

    address = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "address1")
        )
    )

    address.send_keys(ADDRESS)

    print("[OK] Address entered")


    # ========================================================
    # 21. ADDRESS 2
    # ========================================================

    print("\n[21] Filling address 2...")

    address2 = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "address2")
        )
    )

    address2.send_keys(ADDRESS2)

    print("[OK] Address 2 entered")


    # ========================================================
    # 22. POSTAL CODE
    # ========================================================

    print("\n[22] Filling postal code...")

    postalcode = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "postalCode")
        )
    )

    postalcode.send_keys(POSTAL_CODE)

    print("[OK] Postal code entered")


    # ========================================================
    # 23. PHONE
    # ========================================================

    print("\n[23] Filling phone...")

    phone = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "phone")
        )
    )

    phone.send_keys(PHONE)

    print("[OK] Phone entered")


    # ========================================================
    # 24. CITY
    # ========================================================

    print("\n[24] Filling city...")

    city = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "city")
        )
    )

    city.send_keys(CITY)

    print("[OK] City entered")


    # ========================================================
    # 25. PAY NOW BUTTON
    # ========================================================

    print("\n[25] Finding Pay Now button...")

    pay_now = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout-pay-button")
        )
    )

    print("[OK] Pay Now button found")
    print("Displayed:", pay_now.is_displayed())
    print("Enabled:", pay_now.is_enabled())
    print("Text:", pay_now.text)


    # ========================================================
    # 26. CLICK PAY NOW
    # ========================================================

    print("\n[26] Clicking Pay Now...")

    pay_now.click()

    print("[OK] Pay Now clicked")


    # ========================================================
    # 27. FINAL RESULT
    # ========================================================

    print("\n[27] Checking final result...")

    wait.until(
        lambda d: d.current_url != ""
    )

    print("Final URL:", driver.current_url)
    print("Final title:", driver.title)

    page_source_lower = driver.page_source.lower()

    print(
        "Contains 'thank':",
        "thank" in page_source_lower
    )

    print(
        "Contains 'order':",
        "order" in page_source_lower
    )


    # ========================================================
    # 28. SCREENSHOT
    # ========================================================

    print("\n[28] Saving screenshot...")

    driver.save_screenshot(
        "checkout_payment_stage.png"
    )

    print("[OK] Screenshot saved")


    # ========================================================
    # PROJECT SUCCESS
    # ========================================================

    print("\n" + "=" * 70)
    print("FAKERX SELENIUM PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 70)


# ================================================================
# ERROR HANDLING
# ================================================================

except TimeoutException as e:

    print("\n" + "=" * 70)
    print("ERROR TYPE: TIMEOUT")
    print("=" * 70)

    print("Selenium waited for an element/state, but it never appeared.")
    print("Current URL:", driver.current_url)
    print("Current title:", driver.title)

    driver.save_screenshot(
        "ERROR_timeout.png"
    )

    print("Debug screenshot saved: ERROR_timeout.png")


except NoSuchElementException as e:

    print("\n" + "=" * 70)
    print("ERROR TYPE: NO SUCH ELEMENT")
    print("=" * 70)

    print("The requested element does not exist in the DOM.")
    print("Current URL:", driver.current_url)

    driver.save_screenshot(
        "ERROR_no_element.png"
    )

    print("Debug screenshot saved: ERROR_no_element.png")


except ElementClickInterceptedException as e:

    print("\n" + "=" * 70)
    print("ERROR TYPE: CLICK INTERCEPTED")
    print("=" * 70)

    print(
        "The element exists, but another element is blocking "
        "the click."
    )

    print("Current URL:", driver.current_url)

    driver.save_screenshot(
        "ERROR_click_intercepted.png"
    )

    print("Debug screenshot saved: ERROR_click_intercepted.png")


except StaleElementReferenceException as e:

    print("\n" + "=" * 70)
    print("ERROR TYPE: STALE ELEMENT")
    print("=" * 70)

    print(
        "The page replaced the DOM element after Selenium "
        "located it."
    )

    print(
        "FIX: Locate the element again immediately before "
        "using it."
    )

    print("Current URL:", driver.current_url)

    driver.save_screenshot(
        "ERROR_stale_element.png"
    )

    print("Debug screenshot saved: ERROR_stale_element.png")


except WebDriverException as e:

    print("\n" + "=" * 70)
    print("ERROR TYPE: WEBDRIVER")
    print("=" * 70)

    print("A browser/WebDriver-level error occurred.")
    print("Details:", e)
    print("Current URL:", driver.current_url)

    driver.save_screenshot(
        "ERROR_webdriver.png"
    )

    print("Debug screenshot saved: ERROR_webdriver.png")


finally:

    print("\n=== FAKERX SELENIUM PROJECT END ===")

    # Uncomment this when you want Chrome to close automatically.
    # driver.quit()