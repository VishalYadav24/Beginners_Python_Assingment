import argparse
import re


class InvalidCardDuplicateException(Exception):
    {
        "success": "False",
        "message": "More than 4 consecutive numbers are not allowed",
    }
    pass


class InvalidCardInputException(Exception):
    {
        "success": "False",
        "message": "Incorrect input,Please check your card number",
    }
    pass


def count_consecutive_duplicate(card_no: str):
    """Count consecutive duplicate numbers in a string.

    Arguments:
          card_no : string of 16 digit numbers

    Returns :
          True : if number of consecutive numbers is more than allowed limit i.e 4 times
          False : if number of consecutive numbers is less than allowed limit
    """
    repeating_numbers = {}
    duplicates_more_than_allowed = False
    for i in range(0, len((card_no)) - 1):
        if card_no[i] == card_no[i + 1]:
            if repeating_numbers.get(card_no[i]):
                repeating_numbers[card_no[i]] += len(card_no[i])
            else:
                repeating_numbers[card_no[i]] = len(card_no[i])

    for i in repeating_numbers.values():
        print(i)
        if i > 4:
            duplicates_more_than_allowed = True
    return duplicates_more_than_allowed


def validate_credit_card(card_no: str):
    """Valid credit card number provided by user by checking below conditions.
    - Only 16 digits allowed
    - digits can be in group of 4 separated by - hyphen
    - must start with 4 or 5 or 6
    - no consecutive duplicates allowed more than 4 times

    Arguments:
       card_no: str - The card number

    Returns:
      dict -  containing validations result for the card number
    """
    if count_consecutive_duplicate(card_no.replace("-", "")):
        raise InvalidCardDuplicateException
    regex = r"(^[4|5|6]\d{3})-(\d{4})-(\d{4})-(\d{4})"
    match = re.search(regex, card_no)
    if match:
        return {
            "success": "Valid Card",
            "message": "Credit Card number is validated successfully",
        }
    else:
        raise InvalidCardInputException


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate credit card")
    parser.add_argument(
        "card_number",
        metavar="credit card number",
        type=str,
        help="enter your credit card number",
    )
    args: str = parser.parse_args().card_number
    print(validate_credit_card(args))
