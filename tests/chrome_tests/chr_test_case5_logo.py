from selenium.webdriver.common.by import By
from tests.chrome_tests.base_test import BaseTest


class Test1(BaseTest):

    def test_test5(self):
        driver=self.driver

        # test for Logo display. For each view, there is a component tree.
        # Once an issue accrues and causes component tree collapsing
        # sometimes the website work properly but the User is being stuck in Window without errors nor UI.
        # App looks like running properly, with another router-navlink path free from errors
        # however UX effect is terr down to zero.
        # To recognize this issue the easiest way is to check if the simplest element above views
        # directed buy router paths will not be displayed as well as corrupted component tree
        # Failure in such a test gives developer signal something wrong
        # maybe with one of the components in React.Router's paths

        # Second goal is to make sure the Logo of Website Brand is always displayed properly.

        LOGO = self.home_page.get_logo()

        self.home_page.click_reports_button()
        is_displayed = LOGO.is_displayed()
        self.assertTrue(is_displayed)

        self.home_page.click_articles_button()
        is_displayed = LOGO.is_displayed()
        self.assertTrue(is_displayed)

        self.home_page.click_home_button()
        is_displayed = LOGO.is_displayed()
        self.assertTrue(is_displayed)
