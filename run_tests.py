import unittest
from tests.chrome_tests.chr_test_case1_counterbutton import Test1
from tests.chrome_tests.chr_test_case2_menu import Test2
from tests.chrome_tests.chr_test_case3_reports import Test3
from tests.chrome_tests.chr_test_case4_author import Test4
from tests.chrome_tests.chr_test_case5_logo import Test5

chr_test_case1 = unittest.TestLoader().loadTestsFromTestCase(Test1)
chr_test_case2 = unittest.TestLoader().loadTestsFromTestCase(Test2)
chr_test_case3 = unittest.TestLoader().loadTestsFromTestCase(Test3)
chr_test_case4 = unittest.TestLoader().loadTestsFromTestCase(Test4)
chr_test_case5 = unittest.TestLoader().loadTestsFromTestCase(Test5)

tests_for_run = [chr_test_case1, chr_test_case2, chr_test_case3, chr_test_case4, chr_test_case5]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)

