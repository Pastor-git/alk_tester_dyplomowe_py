from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# caps = DesiredCapabilities.FIREFOX.copy()
# caps['marionette'] = False
# driver=webdriver.Firefox(capabilities=caps)

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False
# s = Service("C:/webdrivers/geckodriver.exe")
# driver = webdriver.Chrome(service=s)
driver = webdriver.Firefox(executable_path="C:/webdrivers/geckodriver.exe")

driver.get("https://cabinternational.herokuapp.com")