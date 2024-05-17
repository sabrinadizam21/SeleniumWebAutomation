from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Locators.locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_inputText_id = Locators.username_inputText_id
        self.password_inputText_id = Locators.password_inputText_id
        self.login_button_id = Locators.login_button_id
        self.err_message_xpath = Locators.err_message_xpath

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_inputText_id).clear()
        self.driver.find_element(By.ID, self.username_inputText_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_inputText_id).clear()
        self.driver.find_element(By.ID, self.password_inputText_id).send_keys(password)

    def submit_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

    def login_valid(self, username, password):        
        self.enter_username(username)
        self.enter_password(password)
        self.submit_login()