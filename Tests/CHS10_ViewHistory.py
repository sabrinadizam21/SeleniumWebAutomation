import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.sidebar import Sidebar
from Pages.loginPage import LoginPage
from Pages.historyPage import HistoryPage
from Pages.homePage import Homepage
from Function.main import MainFunc

class ViewHistory(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_view_history(self):
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

        sidebar.click_menu()
        sidebar.click_history()

        # Validation
        historyPage = HistoryPage(driver)
        mainFunc = MainFunc(driver)
        self.assertIn(mainFunc.getContentByXpath(historyPage.visit_date_class), '01/05/2024')
        self.assertIn(mainFunc.getContentByID(historyPage.facility_id), 'Tokyo CURA Healthcare Center')
        self.assertIn(mainFunc.getContentByID(historyPage.hospital_readmission_id), 'Yes')
        self.assertIn(mainFunc.getContentByID(historyPage.program_id), 'Medicare')
        self.assertIn(mainFunc.getContentByID(historyPage.comment_id), 'at 10.00 AM')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()