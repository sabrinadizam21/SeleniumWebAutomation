import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Tests.CHS11_ViewHomepageNoLogin import HomepageNoLogin
from SeleniumWebAutomation.Tests.CHS12_ViewHomepageLogin import HomepageLogin
from SeleniumWebAutomation.Tests.CHS13_ViewProfile import ViewProfile

view_homepage_no_login = unittest.TestLoader().loadTestsFromTestCase(HomepageNoLogin)
view_homepage_login = unittest.TestLoader().loadTestsFromTestCase(HomepageLogin)
view_profile =unittest.TestLoader().loadTestsFromTestCase(ViewProfile)

# create a test suite combining test cases
test_suite = unittest.TestSuite(
    [view_homepage_no_login, view_homepage_login, view_profile]
)

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)