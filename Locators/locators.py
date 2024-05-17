class Locators():

    # Login page locators
    username_inputText_id = 'txt-username'
    password_inputText_id = 'txt-password'
    login_button_id = 'btn-login'
    err_message_xpath = '//*[@class = "lead text-danger" and (text() = "Login failed! Please ensure the username and password are valid." or . = "Login failed! Please ensure the username and password are valid.")]'

    # Sidebar locators
    menu_button_id = 'menu-toggle'
    home_menu_xpath = '//a[@href = "./" and (text() = "Home" or . = "Home")]'
    login_menu_xpath = '//a[@href = "profile.php#login" and (text() = "Login" or . = "Login")]'
    logout_menu_xpath = '//a[@href = "authenticate.php?logout" and (text() = "Logout" or . = "Logout")]'
    history_menu_xpath = '//a[@href = "history.php#history" and (text() = "History" or . = "History")]'
    profile_menu_xpath = '//a[@href = "profile.php#profile" and (text() = "Profile" or . = "Profile")]'

    # Homepage locators
    make_appointment_section_id = 'appointment'
    make_appointment_btn_id = 'btn-make-appointment'
    facility_dropdown_id = 'combo_facility' 
        # Tokyo CURA Healthcare Center
        # Hongkong CURA Healthcare Center
        # Seoul CURA Healthcare Center
    hospital_readmission_checkbox_id = 'chk_hospotal_readmission'
    program_medicare_checkbox_id = 'radio_program_medicare'
    program_medicaid_checkbox_id = 'radio_program_medicaid'
    program_none_checkbox_id = 'radio_program_none'
    visit_date_picker_id = 'txt_visit_date'
    comment_textarea_id = 'txt_comment'
    book_appointment_btn_id = 'btn-book-appointment'
    go_to_homepage_btn_xpath = '//a[@href="https://katalon-demo-cura.herokuapp.com/" and (text() = "Go to Homepage" or . = "Go to Homepage")]'


    # History page locators
    history_section_id = 'history'
    visit_date_class = '//div[@class="panel-heading"]'
    facility_id = 'facility'
    hospital_readmission_id = 'hospital_readmission'
    program_id = 'program'
    comment_id = 'comment'
    go_to_homepage_btn_xpath = '//a[@href="https://katalon-demo-cura.herokuapp.com/" and (text() = "Go to Homepage" or . = "Go to Homepage")]'
    no_appointment_section_xpath = '//p[(text() = "No appointment." or . = "No appointment.")]'
