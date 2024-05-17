import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.sidebar import Sidebar
from Pages.homePage import Homepage
from Function.main import MainFunc

class HomepageLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_view_homepage_after_login(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')

        mainFunction = MainFunc(driver)
        mainFunction.login('John Doe', 'ThisIsNotAPassword')
        time.sleep(1)

        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_home()

        # Validation
        homepage = Homepage(driver)
        driver.find_element(By.ID, homepage.make_appointment_btn_id).is_displayed()
        driver.find_element(By.ID, homepage.make_appointment_section_id).is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()