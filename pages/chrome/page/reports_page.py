from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# deprecated
# driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")

driver.get("https://cabinternational.herokuapp.com/reports")
wait = webdriver(driver, 40) #Explict wait