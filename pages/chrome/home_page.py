from pages.chrome.base_page import BasePage
from pages.chrome.locators import Home_Page_Locators


class Home_Page(BasePage):

    def open_home_page (self, driver):
        self.driver.get("https://cabinternational.herokuapp.com")

    def open_reports_page (self, driver):
        self.driver.get("https://cabinternational.herokuapp.com/reports")

    def open_articles_page (self, driver):
        self.driver.get("https://cabinternational.herokuapp.com/articles")

    def click_button1(self):
        button = self.driver.find_element(*Home_Page_Locators.TEST_BUTTON)
        button.click()

    def click_button2(self):
        button = self.driver.find_element(*Home_Page_Locators.SECOND_BUTTON)
        button.click()

    def get_value_counterbutton(self):
        return self.driver.find_element(*Home_Page_Locators.TEST_BUTTON).text

    def get_value_secondbutton(self):
        return self.driver.find_element(*Home_Page_Locators.SECOND_BUTTON).text

    def click_home_button(self):
        self.driver.find_element(*Home_Page_Locators.HOME_PAGE_BUTTON).click()

    def click_reports_button(self):
        self.driver.find_element(*Home_Page_Locators.REPORTS_PAGE_BUTTON).click()

    def click_articles_button(self):
        self.driver.find_element(*Home_Page_Locators.ARTICLES_PAGE_BUTTON).click()