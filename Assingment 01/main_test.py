import unittest
from main import check_input, check_pnr_status


class TestPnrStatus(unittest.TestCase):
    def test_valid_input(self):
        # Test when input is 10 digits number
        self.assertTrue(check_input("8645658215"))
        # Test when input is less than 10 digits
        self.assertRaises(Exception, check_input, "123")
        # Test when input is alphanumeric
        self.assertRaises(Exception, check_input, "123abc")

    def test_pnr_status(self):
        mocked_response = {
            "success": True,
            "boarding_at": "Jabalpur",
            "arrival_at": "Gorakhpur Jn",
            "seat_info": {"coach": "S5", "berth": "13", "noOfSeats": 1},
        }
        # Test when input is 10 digits number
        self.assertTrue(check_input("8645658215"))
        # Test when input is less than 10 digits
        self.assertRaises(Exception, check_input, "123")
        # Test when input is alphanumeric
        self.assertRaises(Exception, "123abc")
        # Test when input is valid and we get valid response
        self.assertEqual(check_pnr_status("8703198337"), mocked_response)

if __name__ == "__main__":
    unittest.main()