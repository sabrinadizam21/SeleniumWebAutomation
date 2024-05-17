import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Pages.sidebar import Sidebar
from SeleniumWebAutomation.Pages.homePage import Homepage
from SeleniumWebAutomation.Function.main import MainFunc
from SeleniumWebAutomation.Pages.historyPage import HistoryPage

class AddWithoutOptional(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_without_optional_form(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')
        
        mainFunction = MainFunc(driver)
        mainFunction.login('John Doe', 'ThisIsNotAPassword')
        time.sleep(1)

        homePage = Homepage(driver)
        homePage.select_facility('Hongkong CURA Healthcare Center')
        homePage.select_program_medicaid()
        homePage.enter_visit_date('10/05/2024')
        driver.find_element(By.ID, homePage.book_appointment_btn_id).click()
        time.sleep(1)

        # Validation
        driver.find_element(By.ID, 'summary').is_displayed()

        self.assertIn(mainFunction.getContentByID('facility'), 'Hongkong CURA Healthcare Center')
        self.assertIn(mainFunction.getContentByID('hospital_readmission'), 'No')
        self.assertIn(mainFunction.getContentByID('program'), 'Medicaid')
        self.assertIn(mainFunction.getContentByID('visit_date'), '10/05/2024')
        self.assertIn(mainFunction.verifyElementNotDisplay('comment'), 'not exist')

        # Validation display in history page
        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_history()
        historyPage = HistoryPage(driver)
        self.assertIn(mainFunction.getContentByXpath(historyPage.visit_date_class), '10/05/2024')
        self.assertIn(mainFunction.getContentByID(historyPage.facility_id), 'Hongkong CURA Healthcare Center')
        self.assertIn(mainFunction.getContentByID(historyPage.hospital_readmission_id), 'No')
        self.assertIn(mainFunction.getContentByID(historyPage.program_id), 'Medicaid')
        self.assertIn(mainFunction.verifyElementNotDisplay(historyPage.comment_id), 'not exist')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()    





