import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Pages.sidebar import Sidebar
from SeleniumWebAutomation.Pages.loginPage import LoginPage
from SeleniumWebAutomation.Pages.homePage import Homepage

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_login_success(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')
        
        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_login()

        loginPage = LoginPage(driver)
        loginPage.enter_username('John Doe')
        loginPage.enter_password('ThisIsNotAPassword')
        loginPage.submit_login()
        time.sleep(1)

        # Validation
        homepage = Homepage(driver)
        self.driver.find_element(By.ID, homepage.make_appointment_section_id).is_displayed()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()