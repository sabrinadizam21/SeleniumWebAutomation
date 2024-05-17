import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SeleniumWebAutomation.Tests.CHS9_EmptyHistory import EmptyHistory
from SeleniumWebAutomation.Tests.CHS10_ViewHistory import ViewHistory

empty_history = unittest.TestLoader().loadTestsFromTestCase(EmptyHistory)
view_history = unittest.TestLoader().loadTestsFromTestCase(ViewHistory)

# create a test suite combining test cases
test_suite = unittest.TestSuite(
    [empty_history, view_history]
)

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)