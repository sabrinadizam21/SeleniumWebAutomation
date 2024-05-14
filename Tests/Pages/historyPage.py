class HistoryPage():

    def __init__(self, driver):
        self.driver = driver
        self.history_section_id = 'history'
        self.visit_date_class = '//div[@class="panel-heading"]'
        self.facility_id = 'facility'
        self.hospital_readmission_id = 'hospital_readmission'
        self.program_id = 'program'
        self.comment_id = 'comment'
        self.go_to_homepage_btn_xpath = '//a[@href="https://katalon-demo-cura.herokuapp.com/" and (text() = "Go to Homepage" or . = "Go to Homepage")]'
        self.no_appointment_section_xpath = '//p[(text() = "No appointment." or . = "No appointment.")]'
