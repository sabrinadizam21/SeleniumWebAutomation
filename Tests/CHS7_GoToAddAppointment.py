import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.homePage import Homepage
from Function.main import MainFunc

class GoToAddAppointment(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_go_to_appointment_after_create_one(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')
        
        mainFunction = MainFunc(driver)
        mainFunction.login('John Doe', 'ThisIsNotAPassword')
        time.sleep(1)

        # create first
        homePage = Homepage(driver)
        homePage.select_facility('Tokyo CURA Healthcare Center')
        homePage.check_hospital_readmission()
        homePage.select_program_medicare()
        homePage.enter_visit_date('01/05/2024')
        homePage.enter_comment('at 10.00 AM')
        driver.find_element(By.ID, homePage.book_appointment_btn_id).click()
        time.sleep(1)

        # Go to appointment section
        driver.find_element(By.XPATH, homePage.go_to_homepage_btn_xpath).click()
        time.sleep(1)
        homePage.select_facility('Seoul CURA Healthcare Center')
        homePage.check_hospital_readmission()
        homePage.select_program_none()
        homePage.enter_visit_date('15/05/2024')
        homePage.enter_comment('Ontime at 11.00 AM')
        driver.find_element(By.ID, homePage.book_appointment_btn_id).click()
        time.sleep(1)

        # Validation
        driver.find_element(By.ID, 'summary').is_displayed()

        self.assertIn(mainFunction.getContentByID('facility'), 'Seoul CURA Healthcare Center')
        self.assertIn(mainFunction.getContentByID('hospital_readmission'), 'Yes')
        self.assertIn(mainFunction.getContentByID('program'), 'None')
        self.assertIn(mainFunction.getContentByID('visit_date'), '15/05/2024')
        self.assertIn(mainFunction.getContentByID('comment'), 'Ontime at 11.00 AM')

        # Validation display in history page

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()