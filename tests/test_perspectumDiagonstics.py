import unittest
import sys
from StringIO import StringIO

from PerspectumDiagnostics import perspectum_diagnostics_test as pdt


class MyTest(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_example_case(self):
        """
        This unit test method will assert that the output of the application under
        test is as expected.
        :return: Unit test pass or failure
        """
        test_list_in = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
        exepected_string_in_multiple_list = "Strings appearing in multiple lists: 'gh'"
        expected_number_unique_strings = "number of unique strings: 7"
        expected_number_strings_processed = "Total number of strings processed 9"

        pdt(test_list_in)
        self.assertIn(exepected_string_in_multiple_list, sys.stdout.getvalue())
        self.assertIn(expected_number_unique_strings, sys.stdout.getvalue())
        self.assertIn(expected_number_strings_processed, sys.stdout.getvalue())


