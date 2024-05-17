import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Pages.loginPage import LoginPage
from SeleniumWebAutomation.Pages.sidebar import Sidebar

class Logout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_logout_success(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')

        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_login()

        loginPage = LoginPage(driver)
        loginPage.login_valid('John Doe', 'ThisIsNotAPassword')

        sidebar.click_menu()
        sidebar.click_logout()

        # Validation
        sidebar.click_menu()
        driver.find_element(By.XPATH, sidebar.login_menu_xpath).is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

