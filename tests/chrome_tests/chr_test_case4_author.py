from selenium.webdriver.common.by import By
from tests.chrome_tests.base_test import BaseTest


class Test4(BaseTest):

    def test_test4(self):
        driver=self.driver
        self.home_page.open_articles_page(driver)

        # checking if all the articles presented on page has "JAN" as "author"
        # this could prevent website administrators from receiving intellectual property rights delict penalty

        article_list = driver.find_elements(By.CLASS_NAME, "article")
        number_of_articles = len(article_list)
        article_list_author = driver.find_elements(By.XPATH, "//*[contains(text(),'Jan')]")
        number_of_cases = len(article_list_author)
        self.assertEqual(number_of_articles, number_of_cases)