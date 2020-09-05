import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys

sys.path.append("C:\\Users\\User\\PycharmProjects\\PythonUnitTestPOMBased")
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL="https://admin-demo.nopcommerce.com"
    username="admin@youthstore.com"
    password="admin"
    driver=webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\PythonUnitTestPOMBased\\drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        #lp.clickLogin()

        time.sleep(4)

        self.assertNotEqual("Veera Pulapakura",self.driver.title,"Both are equal")
        #lp.clickLogout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("..\\PythonUnitTestPOMBased\\reports"))
