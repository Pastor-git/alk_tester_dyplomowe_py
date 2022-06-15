from selenium.webdriver.common.by import By
from tests.chrome_tests.base_test import BaseTest


class Test1(BaseTest):

    def test_test3(self):
        driver=self.driver
        self.home_page.open_reports_page(driver)

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

        # OK
        # self.assertEqual(5, number_of_cases)