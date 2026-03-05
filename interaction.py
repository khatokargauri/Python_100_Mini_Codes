from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
#Find the first name, last name, and email fields
first_name = driver.find_element(By.NAME, value = "fName")
last_name = driver.find_element(By.NAME, value = "lName")
email = driver.find_element(By.NAME, value = "email")
first_name.send_keys("Gauri")
last_name.send_keys("Khatokar")
email.send_keys("abd@gmail.com")
#Locate the "Sign Up" button. Then click on it
submit = driver.find_element(By.CSS_SELECTOR, value = "form button")
submit.click()

