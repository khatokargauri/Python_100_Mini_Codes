from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

# Select English language
print("Looking for language selection...")
try:
    language_button = driver.find_element(By.ID, "langSelect-EN")
    language_button.click()
    print("English selected")
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

# Accept cookie consent popup
try:
    cookie_accept = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
    cookie_accept.click()
    print("Cookie consent accepted")
    sleep(1)
except NoSuchElementException:
    print("No cookie popup found")

# Find the big cookie
cookie = driver.find_element(By.ID, "bigCookie")

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:
    cookie.click()

    if time() > timeout:
        try:
            # Get cookie count
            cookies_element = driver.find_element(By.ID, "cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split(" ")[0].replace(",", ""))

            # Get all products
            products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")

            best_item = None

            # Check most expensive first
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't read cookie count or buy item")

        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, "cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break