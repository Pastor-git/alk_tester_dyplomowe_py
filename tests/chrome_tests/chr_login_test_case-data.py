from selenium.webdriver.common.by import By
from tests.chrome_tests.base_test import BaseTest
from tests.chrome_tests.test_data import TestData


class Test1(BaseTest):

    def test_login(self):
        driver = self.driver

        # TEST DATA:
        login = "login"
        password = "password"

        login_input = driver.find_element(By.ID, 'login')
        login_input.send_keys(login)

        password_input = driver.find_element(By.ID, 'pass')
        password_input.send_keys(password)

        button_login = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/button")
        button_login.click()

    #Login system with FireBase will be developed