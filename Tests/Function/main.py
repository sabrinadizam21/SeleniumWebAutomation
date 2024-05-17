from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from Pages.loginPage import LoginPage
from Pages.sidebar import Sidebar

class MainFunc():
    
    def __init__(self, driver):
        self.driver = driver
    
    def getContentByID(self, id):
        content = self.driver.find_element(By.ID, id).text
        return content
    
    def getContentByXpath(self, xpath):
        content = self.driver.find_element(By.XPATH, xpath).text
        return content
    
    def verifyElementNotDisplay(self, id):
        try:
            element = self.driver.find_element(By.ID, id)
            return 'exist'
        except NoSuchElementException:
            return 'not exist'
        
    def login(self, username, password):
        sidebar = Sidebar(self.driver)
        sidebar.click_menu()
        sidebar.click_login()

        loginPage = LoginPage(self.driver)
        loginPage.enter_username(username)
        loginPage.enter_password(password)
        loginPage.submit_login()