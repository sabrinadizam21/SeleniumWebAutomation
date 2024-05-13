from selenium.webdriver.common.by import By

class Homepage():
    def __init__(self, driver):
        self.driver = driver
        self.make_appointment_section_id = 'appointment'
        self.facility_dropdown_id = 'combo_facility' 
            # Tokyo CURA Healthcare Center
            # Hongkong CURA Healthcare Center
            # Seoul CURA Healthcare Center
        self.hospital_readmission_checkbox_id = 'chk_hospotal_readmission'
        self.program_medicare_checkbox_id = 'radio_program_medicare'
        self.program_medicaid_checkbox_id = 'radio_program_medicaid'
        self.program_none_checkbox_id = 'radio_program_none'
        self.visit_date_picker_id = 'txt_visit_date'
        self.comment_textarea_id = 'txt_comment'
        self.book_appointment_btn_id = 'btn-book-appointment'
        self.go_to_homepage_btn_xpath = '//a[@href="https://katalon-demo-cura.herokuapp.com/" and (text() = "Go to Homepage" or . = "Go to Homepage")]'

    def select_facility(self, facility):
        self.driver.find_element(By.ID, self.facility_dropdown_id).send_keys(facility)

    def check_hospital_readmission(self):
        self.driver.find_element(By.ID, self.hospital_readmission_checkbox_id).click()

    def select_program_medicare(self):
        self.driver.find_element(By.ID, self.program_medicare_checkbox_id).click()

    def select_program_medicaid(self):
        self.driver.find_element(By.ID, self.program_medicaid_checkbox_id).click()

    def select_program_none(self):
        self.driver.find_element(By.ID, self.program_none_checkbox_id).click()

    def enter_visit_date(self, visit_date):
        self.driver.find_element(By.ID, self.visit_date_picker_id).clear()
        self.driver.find_element(By.ID, self.visit_date_picker_id).send_keys(visit_date)

    def enter_comment(self, comment):
        self.driver.find_element(By.ID, self.comment_textarea_id).clear()
        self.driver.find_element(By.ID, self.comment_textarea_id).send_keys(comment)