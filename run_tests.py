import unittest
from tests.chrome_tests import chr_test_case1
from tests.chrome_tests import chr_test_case2
from tests.chrome_tests import chr_test_case3
from tests.chrome_tests import chr_test_case4
from tests.chrome_tests import chr_test_case5

# Pobierz testy, które chcesz uruchomić
registration_test = unittest.TestLoader().loadTestsFromTestCase(
    chr_test_case1,
    chr_test_case2,
    chr_test_case3,
    chr_test_case4,
    chr_test_case5)

# Lista testów do uruchomienia
tests_for_run = [
    chr_test_case1,
    chr_test_case2,
    chr_test_case3,
    chr_test_case4,
    chr_test_case5
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)

# Odpal testy
unittest.TextTestRunner().run(test_suite)