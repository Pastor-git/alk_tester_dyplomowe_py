import unittest
from tests.chrome_tests import chr_test_case1_counterbutton
from tests.chrome_tests import chr_test_case2_menu
from tests.chrome_tests import chr_test_case3_reports
from tests.chrome_tests import chr_test_case4_author
from tests.chrome_tests import chr_test_case5_logo

registration_test = unittest.TestLoader().loadTestsFromTestCase(chr_test_case1)

tests_for_run = [
    chr_test_case1,
    chr_test_case2,
    chr_test_case3,
    chr_test_case4,
    chr_test_case5
]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)