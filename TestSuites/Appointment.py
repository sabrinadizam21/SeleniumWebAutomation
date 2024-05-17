import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Tests.CHS5_Add_Appointment import AddAppointment
from SeleniumWebAutomation.Tests.CHS6_Add_without_optional import AddWithoutOptional
from SeleniumWebAutomation.Tests.CHS7_GoToAddAppointment import GoToAddAppointment
from SeleniumWebAutomation.Tests.CHS8_FailedAddAppointment import FailedAddAppointment

add_appointment = unittest.TestLoader().loadTestsFromTestCase(AddAppointment)
add_without_optional = unittest.TestLoader().loadTestsFromTestCase(AddWithoutOptional)
go_to_add_appointment =unittest.TestLoader().loadTestsFromTestCase(GoToAddAppointment)
failed_add_appointment =unittest.TestLoader().loadTestsFromTestCase(FailedAddAppointment)

# create a test suite combining test cases
test_suite = unittest.TestSuite(
    [add_appointment, add_without_optional, go_to_add_appointment, failed_add_appointment]
)

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)