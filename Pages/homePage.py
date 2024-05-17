from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Locators.locators import Locators

class Homepage():
    def __init__(self, driver):
        self.driver = driver
        self.make_appointment_section_id = Locators.make_appointment_section_id
        self.make_appointment_btn_id = Locators.make_appointment_btn_id
        self.facility_dropdown_id = Locators.facility_dropdown_id
            # Tokyo CURA Healthcare Center
            # Hongkong CURA Healthcare Center
            # Seoul CURA Healthcare Center
        self.hospital_readmission_checkbox_id = Locators.hospital_readmission_checkbox_id
        self.program_medicare_checkbox_id = Locators.program_medicare_checkbox_id
        self.program_medicaid_checkbox_id = Locators.program_medicaid_checkbox_id
        self.program_none_checkbox_id = Locators.program_none_checkbox_id
        self.visit_date_picker_id = Locators.visit_date_picker_id
        self.comment_textarea_id = Locators.comment_textarea_id
        self.book_appointment_btn_id = Locators.book_appointment_btn_id
        self.go_to_homepage_btn_xpath = Locators.go_to_homepage_btn_xpath

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