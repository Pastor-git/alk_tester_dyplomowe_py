from selenium.webdriver.common.by import By
from tests.chrome_tests.base_test import BaseTest


class Test1(BaseTest):

    def test_test1(self):

        # Testing build-in functionality inside the second button build from instance of React.Component CounterButton
        # without any unique property - simulation of non-supportive-tester environment

        number1 = self.home_page.get_value_secondbutton()
        self.home_page.click_button2()
        number2 = self.home_page.get_value_secondbutton()
        self.assertNotEqual(number1, number2)

        # testing inf each instance of CounterButton is independent and has independent result based on "props"
        # without interfering with state of data button2.number should be higher than not-clicked button1.number
        # any locator other than XPATH should lead to the CounterButton instance displayed as first

        number1 = self.home_page.get_value_secondbutton()
        number2 = self.home_page.get_value_counterbutton()
        self.assertNotEqual(number1, number2)