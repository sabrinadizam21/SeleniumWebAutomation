import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.sidebar import Sidebar
from Function.main import MainFunc

class ViewProfile(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_view_profile_page(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')

        mainFunction = MainFunc(driver)
        mainFunction.login('John Doe', 'ThisIsNotAPassword')
        time.sleep(1)

        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_profile()

        # Validation
        driver.find_element(By.XPATH, '//h2[(text = "Profile" or . = "Profile")]').is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()