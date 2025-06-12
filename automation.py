''''
This script uses Selenium to automate a Firefox browser.
It opens a webpage, checks the title, navigates and test to a demo site.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service(executable_path='./geckodriver')
firefox_browser = webdriver.Firefox(service=service)
firefox_browser.get('https://www.google.com')

print('Google' in firefox_browser.title) # give True

# assert 'Googles' in firefox_browser.title # if False trows an AsserError

print(firefox_browser.page_source)  # Get the page source

firefox_browser.get("https://tutorialsninja.com/demo/")  # Navigate to another page

time.sleep(1)  # Wait for 1 seconds

button = firefox_browser.find_element(By.CLASS_NAME, "btn.btn-inverse.btn-block.btn-lg.dropdown-toggle")  # Find an element by class name 
# the selector here was btn btn-inverse btn-block btn-lg dropdown-toggle

button.click()  # Click the button

button_innerHTML = button.get_attribute("innerHTML")  # Get the text of the button
print("Inner HTML: \n"+ button_innerHTML)  # Print the button text
print("Text of the button: " + button.text)  # Print text of the button


firefox_browser.find_element(By.NAME, "search").send_keys("Selenium")  # Find the search input and type "Selenium"
time.sleep(1)  # Wait for 1 seconds

#firefox_browser.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()  # Click the search button with class name
firefox_browser.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-lg").click()  # Click the search button with CSS selector

time.sleep(2)  # Wait for 2 seconds

firefox_browser.back()  # Go back to the previous page

time.sleep(4)  # Wait for 4 seconds
firefox_browser.quit()  # Close the browser after use
