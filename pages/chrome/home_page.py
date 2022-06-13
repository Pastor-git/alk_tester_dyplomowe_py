from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from locators import element
from selenium.webdriver.common.by import By

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# deprecated
# driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")

driver.get("https://cabinternational.herokuapp.com")
driver.maximize_window()
element2 = driver.find_element_by_id('testbutton')
print(type(element2))
print(element2)
print(driver.current_url)
# print(driver.page_source)
element2.click()

element.click()
home_page = driver.get("https://cabinternational.herokuapp.com")