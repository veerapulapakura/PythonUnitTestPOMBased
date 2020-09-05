from selenium import webdriver
import pytest

class TestReports():

    @pytest.fixture()
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\PythonUnitTestPOMBased\\drivers\\chromedriver.exe")
        self.driver.maximize_window()

        yield
        self.driver.close()

    def test_Testmethod(self,setUp):
        self.driver.get("https://www.google.co.uk/")
        assert self.driver.title == "Google"




