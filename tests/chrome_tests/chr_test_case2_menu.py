from selenium.webdriver.common.by import By
from tests.chrome_tests.base_test import BaseTest


class Test2(BaseTest):

    def test_test2(self):
        driver=self.driver

        #check if menu <div> and buttons representing React.Router and React.Navlink are displayed:

        is_displayed = self.home_page.is_menu_displayed
        self.assertTrue(is_displayed)

        is_displayed = self.home_page.is_home_displayed
        self.assertTrue(is_displayed)

        is_displayed = self.home_page.is_reports_displayed
        self.assertTrue(is_displayed)

        is_displayed = self.home_page.is_articles_displayed
        self.assertTrue(is_displayed)

        #checking the views handled/wrapped by Router:

        self.home_page.click_reports_button()
        current_url = driver.current_url
        expected_url = "https://cabinternational.herokuapp.com/reports"
        self.assertEqual(current_url, expected_url)

        self.home_page.click_articles_button()
        current_url = driver.current_url
        expected_url = "https://cabinternational.herokuapp.com/articles"
        self.assertEqual(current_url, expected_url)

        self.home_page.click_home_button()
        current_url = driver.current_url
        expected_url = "https://cabinternational.herokuapp.com/"
        self.assertEqual(current_url, expected_url)
