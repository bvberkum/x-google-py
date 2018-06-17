import unittest


def test_0_1_assert_true():
    assert True

class NullUnitTestCase(unittest.TestCase):
    def test_0_2_testcase_assert_true(self):
        assert True

def test_0_3_import():
    import x_google_py
    import x_google_py.creds
