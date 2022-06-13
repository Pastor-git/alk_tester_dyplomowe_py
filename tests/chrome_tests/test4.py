import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Test1(unittest.TestCase):
    def setUp(self):
        s = Service("C:\webdrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://cabinternational.herokuapp.com")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_test1(self):
        driver=self.driver

if __name__ == "__main__":
    unittest.main()