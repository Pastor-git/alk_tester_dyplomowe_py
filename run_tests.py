import unittest
from unittest import TestLoader, TestSuite, TextTestRunner
from tests.chrome_tests import chr_test_case1_counterbutton
from tests.chrome_tests import chr_test_case2_menu
from tests.chrome_tests import chr_test_case3_reports
from tests.chrome_tests import chr_test_case4_author
from tests.chrome_tests import chr_test_case5_logo

chr_test_case1 = unittest.TestLoader().loadTestsFromTestCase(chr_test_case1_counterbutton)
# chr_test_case2 = unittest.TestLoader().loadTestsFromTestCase(chr_test_case2_menu)
# chr_test_case3 = unittest.TestLoader().loadTestsFromTestCase(chr_test_case3_reports)
# chr_test_case4 = unittest.TestLoader().loadTestsFromTestCase(chr_test_case4_author)
# chr_test_case5 = unittest.TestLoader().loadTestsFromTestCase(chr_test_case5_logo)

tests_for_run = [chr_test_case1]

# , chr_test_case2, chr_test_case3, chr_test_case4, chr_test_case5
test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)

# example_tests = TestLoader().loadTestsFromTestCase(tests_for_run)
# suite = TestSuite(example_tests)
# runner = TextTestRunner()
# runner.run(suite)