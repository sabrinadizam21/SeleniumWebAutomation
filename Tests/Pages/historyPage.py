from Locators.locators import Locators

class HistoryPage():

    def __init__(self, driver):
        self.driver = driver
        self.history_section_id = Locators.history_section_id
        self.visit_date_class = Locators.visit_date_class
        self.facility_id = Locators.facility_id
        self.hospital_readmission_id = Locators.hospital_readmission_id
        self.program_id = Locators.program_id
        self.comment_id = Locators.comment_id
        self.go_to_homepage_btn_xpath = Locators.go_to_homepage_btn_xpath
        self.no_appointment_section_xpath = Locators.no_appointment_section_xpath
