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

        # Testing build-in functionality inside the second button build from instance of React.Component CounterButton
        # without any unique property - simulation of non-supportive-tester environment

        driver=self.driver
        button2 = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/button')
        number1 = button2.text
        button2.click()
        number2 = button2.text
        self.assertNotEqual(number1, number2)

        # testing inf each instance of CounterButton is independent and has independent result based on "props"
        # without interfering with state of data button2.number should be higher than not-clicked button1.number
        # any locator other than XPATH should lead to the CounterButton instance displayed as first

        button1 = driver.find_element(By.ID, 'testbutton')
        number1 = button1.text
        number2 = button2.text
        self.assertNotEqual(number1, number2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()