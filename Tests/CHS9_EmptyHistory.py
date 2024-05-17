import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Pages.sidebar import Sidebar
from SeleniumWebAutomation.Function.main import MainFunc
from SeleniumWebAutomation.Pages.historyPage import HistoryPage

class EmptyHistory(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_empty_history(self):
        driver = self.driver
        driver.get('https://katalon-demo-cura.herokuapp.com/')

        mainFunction = MainFunc(driver)
        mainFunction.login('John Doe', 'ThisIsNotAPassword')
        time.sleep(1)

        sidebar = Sidebar(driver)
        sidebar.click_menu()
        sidebar.click_history()

        # Validation
        historyPage = HistoryPage(driver)
        driver.find_element(By.XPATH, historyPage.no_appointment_section_xpath).is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()