import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Test1(unittest.TestCase):
    def setUp(self):
        s = Service("C:\webdrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://cabinternational.herokuapp.com/reports")
        self.driver.maximize_window()

    def test_test1(self):
        driver=self.driver

        #checking number of "reports"/company products displayed on page with knowledge of exact number
        # which should be displayed as an input for the test case

        report_list = driver.find_elements(By.CLASS_NAME, "report")
        number_of_reports = len(report_list)
        self.assertEqual(4, number_of_reports)

        #based on confirming all the reports are displayed, the test case should check for developer mistakes
        # resulting in errors or issues presenting critical information or code value on the website
        # conditions expected: 0 - for training purposes test will fail deliberately

        report_list_error = driver.find_elements(By.XPATH, "//*[contains(text(),'/static/media/')]")
        number_of_cases = len(report_list_error)
        self.assertEqual(0, number_of_cases)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()