import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.sidebar import Sidebar
from Function.main import MainFunc
from Pages.homePage import Homepage

class HomepageNoLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_view_homepage_without_login(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')

        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_home()

        # Validation
        mainFunc = MainFunc(driver)
        homepage = Homepage(driver)
        driver.find_element(By.ID, homepage.make_appointment_btn_id).is_displayed()
        isExist = mainFunc.verifyElementNotDisplay(homepage.make_appointment_section_id)
        self.assertIn(isExist, 'not exist')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()