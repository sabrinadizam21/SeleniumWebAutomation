from selenium.webdriver.common.by import By
from Locators.locators import Locators

class Sidebar():
    def __init__(self, driver):
        self.driver = driver
        self.menu_button_id = Locators.menu_button_id
        self.home_menu_xpath = Locators.home_menu_xpath
        self.login_menu_xpath = Locators.login_menu_xpath
        self.logout_menu_xpath = Locators.logout_menu_xpath
        self.history_menu_xpath = Locators.history_menu_xpath
        self.profile_menu_xpath = Locators.profile_menu_xpath
    
    def click_menu(self):
        self.driver.find_element(By.ID, self.menu_button_id).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_menu_xpath).click()

    def click_history(self):
        self.driver.find_element(By.XPATH, self.history_menu_xpath).click()

    def click_profile(self):
        self.driver.find_element(By.XPATH, self.profile_menu_xpath).click()

    def click_home(self):
        self.driver.find_element(By.XPATH, self.home_menu_xpath).click()