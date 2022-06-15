from pages.chrome.home_page import Home_Page
from tests.chrome_tests.test_data import TestData
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        s = Service("C:\webdrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        # LINUX:
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://cabinternational.herokuapp.com")
        self.home_page = Home_Page(self.driver)
        Home_Page.open_home_page(self, self.driver)
        self.driver.maximize_window()
        # self.test_data = TestData()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()