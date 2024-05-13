import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.sidebar import Sidebar
from Pages.loginPage import LoginPage
from Pages.homePage import Homepage
from Function.main import MainFunc

class AddWithoutOptional(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_without_optional_form(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')

        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_login()

        loginPage = LoginPage(driver)
        loginPage.login_valid('John Doe', 'ThisIsNotAPassword')
        time.sleep(1)

        homePage = Homepage(driver)
        homePage.select_facility('Hongkong CURA Healthcare Center')
        homePage.select_program_medicaid()
        homePage.enter_visit_date('10/05/2024')
        driver.find_element(By.ID, homePage.book_appointment_btn_id).click()
        time.sleep(1)

        # Validation
        driver.find_element(By.ID, 'summary').is_displayed()

        mainFunction = MainFunc(driver)
        self.assertIn(mainFunction.getContentByID('facility'), 'Hongkong CURA Healthcare Center')
        self.assertIn(mainFunction.getContentByID('hospital_readmission'), 'No')
        self.assertIn(mainFunction.getContentByID('program'), 'Medicaid')
        self.assertIn(mainFunction.getContentByID('visit_date'), '10/05/2024')
        self.assertIn(mainFunction.verifyElementNotDisplay('comment'), 'not exist')

        # Validation display in history page

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()    





