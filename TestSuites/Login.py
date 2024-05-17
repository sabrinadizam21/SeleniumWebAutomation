import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Tests.CHS1_LoginSuccess import Login
from SeleniumWebAutomation.Tests.CHS2_InvalidUsername import LoginFailed as InvalidUsername
from SeleniumWebAutomation.Tests.CHS3_InvalidPassword import LoginFailed as InvalidPassword
from SeleniumWebAutomation.Tests.CHS4_Logout import Logout

# get all tests from all test case class
login_success = unittest.TestLoader().loadTestsFromTestCase(Login)
login_failed_invalid_username = unittest.TestLoader().loadTestsFromTestCase(InvalidUsername)
login_failed_invalid_password = unittest.TestLoader().loadTestsFromTestCase(InvalidPassword)
logout_success = unittest.TestLoader().loadTestsFromTestCase(Logout)

# create a test suite combining test cases
test_suite = unittest.TestSuite(
    [login_success, login_failed_invalid_username, login_failed_invalid_password, logout_success]
)

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)