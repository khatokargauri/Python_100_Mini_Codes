from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers = header)
data = response.text
soup = BeautifulSoup(data, "html.parser")
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} links to individual listings in total : \n")
print(all_links)
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace("|", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this : \n")
print(all_addresses)
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this : \n")
print(all_prices)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
form_link = "https://docs.google.com/forms/d/e/1FAIpQLSfV3rgfbJHeddskjzN-fppZLIVZ2eESMlJpa35T-qGd6nkBQw/viewform?usp=dialog"
for n in range(len(all_links)):
    driver.get(form_link)
    time.sleep(3)
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    address = inputs[0]
    price = inputs[1]
    link = inputs[2]
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()
    time.sleep(2)
