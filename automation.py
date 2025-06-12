from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service(executable_path='./geckodriver')
firefox_browser = webdriver.Firefox(service=service)
firefox_browser.get('https://www.google.com')
