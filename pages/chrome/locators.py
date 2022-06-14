# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# s = Service("C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
#
# driver.get("https://cabinternational.herokuapp.com")
# driver.maximize_window()
# element = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/button')
# element.click()

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass