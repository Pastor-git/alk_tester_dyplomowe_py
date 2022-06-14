import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Test1(unittest.TestCase):
    def setUp(self):
        s = Service("C:\webdrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://cabinternational.herokuapp.com/articles")
        self.driver.maximize_window()

    def test_test1(self):
        driver=self.driver

        # checking if all the articles presneted on page has "JAN" as "author"
        # this could prevent website administrators from receiving intellectual property rights delict penalty

        article_list = driver.find_elements(By.CLASS_NAME, "article")
        number_of_articles = len(article_list)
        article_list_author = driver.find_elements(By.XPATH, "//*[contains(text(),'Jan')]")
        number_of_cases = len(article_list_author)
        self.assertEqual(number_of_articles, number_of_cases)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()