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

        #Locators by exact XPATH:

        MAIN_DIV = driver.find_element(By.XPATH, "/html/body/div[1]/nav")
        HOME_PAGE_BUTTON = driver.find_element(By.XPATH, "/html/body/div[1]/nav/table/tr[1]/a/button")
        REPORTS_PAGE_BUTTON = driver.find_element(By.XPATH, "/html/body/div[1]/nav/table/tr[2]/a/button")
        ARTICLES_PAGE_BUTTON = driver.find_element(By.XPATH, "/html/body/div[1]/nav/table/tr[3]/a/button")

        #check if menu <div> and buttons representing React.Router and React.Navlink are displayed:

        is_displayed = MAIN_DIV.is_displayed()
        self.assertTrue(is_displayed)

        is_displayed = HOME_PAGE_BUTTON.is_displayed()
        self.assertTrue(is_displayed)

        is_displayed = REPORTS_PAGE_BUTTON.is_displayed()
        self.assertTrue(is_displayed)

        is_displayed = ARTICLES_PAGE_BUTTON.is_displayed()
        self.assertTrue(is_displayed)

        #checking the views handled/wrapped by Router:

        REPORTS_PAGE_BUTTON.click()
        current_url = driver.current_url
        expected_url = "https://cabinternational.herokuapp.com/reports"
        self.assertEqual(current_url, expected_url)

        ARTICLES_PAGE_BUTTON.click()
        current_url = driver.current_url
        expected_url = "https://cabinternational.herokuapp.com/articles"
        self.assertEqual(current_url, expected_url)

        HOME_PAGE_BUTTON.click()
        current_url = driver.current_url
        expected_url = "https://cabinternational.herokuapp.com/"
        self.assertEqual(current_url, expected_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()