from selenium.webdriver.common.by import By

class Sidebar():
    def __init__(self, driver):
        self.driver = driver
        self.menu_button_id = 'menu-toggle'
        self.login_menu_xpath = '//a[@href = "profile.php#login" and (text() = "Login" or . = "Login")]'
        self.logout_menu_xpath = '//a[@href = "authenticate.php?logout" and (text() = "Logout" or . = "Logout")]'
    
    def click_menu(self):
        self.driver.find_element(By.ID, self.menu_button_id).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_menu_xpath).click()