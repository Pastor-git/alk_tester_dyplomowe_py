from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#WINDOWS:
# s = Service("C:/webdrivers/geckodriver.exe")
# driver = webdriver.Chrome(service=s)

driver = webdriver.Firefox(executable_path="C:/webdrivers/geckodriver.exe")

driver.get("https://cabinternational.herokuapp.com")
driver.maximize_window()

# LINUX:
# driver = webdriver.Chrome()