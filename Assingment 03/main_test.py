import unittest
from main import (
    validate_credit_card,
    InvalidCardDuplicateException,
    InvalidCardInputException,
)


class TestValidateCreditCard(unittest.TestCase):
    def test_validate_credit_card(self):
        valid_input = "4234-5678-9870-1004"
        invalid_input = "1234-4567-5688-8888"
        invalid_length_input = "1234"
        valid_response = {
            "success": "Valid Card",
            "message": "Credit Card number is validated successfully",
        }
        # Testing with valid case
        self.assertEquals(validate_credit_card(valid_input), valid_response)
        # Testing with invalid case
        self.assertRaises(
            InvalidCardDuplicateException, validate_credit_card, invalid_input
        )
        # Testing with invalid case
        self.assertRaises(
            InvalidCardInputException, validate_credit_card, invalid_length_input
        )


if __name__ == "__main__":
    unittest.main()
