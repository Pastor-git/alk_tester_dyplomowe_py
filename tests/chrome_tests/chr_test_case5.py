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

    def test_test1(self):
        driver=self.driver


        LOGO = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/img")
        HOME_PAGE_BUTTON = driver.find_element(By.XPATH, "/html/body/div[1]/nav/table/tr[1]/a/button")
        REPORTS_PAGE_BUTTON = driver.find_element(By.XPATH, "/html/body/div[1]/nav/table/tr[2]/a/button")
        ARTICLES_PAGE_BUTTON = driver.find_element(By.XPATH, "/html/body/div[1]/nav/table/tr[3]/a/button")

        REPORTS_PAGE_BUTTON.click()
        is_displayed = LOGO.is_displayed()
        self.assertTrue(is_displayed)

        ARTICLES_PAGE_BUTTON.click()
        is_displayed = LOGO.is_displayed()
        self.assertTrue(is_displayed)

        HOME_PAGE_BUTTON.click()
        is_displayed = LOGO.is_displayed()
        self.assertTrue(is_displayed)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()