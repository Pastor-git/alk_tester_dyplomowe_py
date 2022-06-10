from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# deprecated
# driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")

driver.get("https://cabinternational.herokuapp.com/reports")