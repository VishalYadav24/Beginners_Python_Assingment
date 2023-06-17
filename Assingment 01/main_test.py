import unittest
from main import check_input, check_pnr_status


class TestPnrStatus(unittest.TestCase):
    def test_valid_input(self):
        # Test when input is 10 digits number
        self.assertTrue(check_input("8645658215"))
        # Test when input is less than 10 digits
        self.assertRaises(Exception, "123")
        # Test when input is alphanumeric
        self.assertRaises(Exception, "123abc")

    def test_pnr_status(self):
        # Test when input is 10 digits number
        self.assertTrue(check_input("8645658215"))
        # Test when input is less than 10 digits
        self.assertRaises(Exception, "123")
        # Test when input is alphanumeric
        self.assertRaises(Exception, "123abc")
        # Test when input is valid and we get valid response
        self.assertEqual(check_pnr_status('8703198337'),200)