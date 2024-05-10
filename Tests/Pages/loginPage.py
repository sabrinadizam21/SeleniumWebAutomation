from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_inputText_id = 'txt-username'
        self.password_inputText_id = 'txt-password'
        self.login_button_id = 'btn-login'
        self.err_message_xpath = '//*[@class = "lead text-danger" and (text() = "Login failed! Please ensure the username and password are valid." or . = "Login failed! Please ensure the username and password are valid.")]'

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