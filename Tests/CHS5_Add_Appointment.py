import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.sidebar import Sidebar
from Pages.loginPage import LoginPage
from Pages.homePage import Homepage
from Function.main import MainFunc

class AddAppointment(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_input_all_forms(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')

        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_login()

        loginPage = LoginPage(driver)
        loginPage.login_valid('John Doe', 'ThisIsNotAPassword')
        time.sleep(1)

        homePage = Homepage(driver)
        homePage.select_facility('Tokyo CURA Healthcare Center')
        homePage.check_hospital_readmission()
        homePage.select_program_medicare()
        homePage.enter_visit_date('01/05/2024')
        homePage.enter_comment('at 10.00 AM')
        driver.find_element(By.ID, homePage.book_appointment_btn_id).click()
        time.sleep(1)

        # Validation
        driver.find_element(By.ID, 'summary').is_displayed()

        mainFunction = MainFunc(driver)
        self.assertIn(mainFunction.getContentByID('facility'), 'Tokyo CURA Healthcare Center')
        self.assertIn(mainFunction.getContentByID('hospital_readmission'), 'Yes')
        self.assertIn(mainFunction.getContentByID('program'), 'Medicare')
        self.assertIn(mainFunction.getContentByID('visit_date'), '01/05/2024')
        self.assertIn(mainFunction.getContentByID('comment'), 'at 10.00 AM')

        # Validation display in history page
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()    





