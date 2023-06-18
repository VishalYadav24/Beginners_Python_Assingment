import argparse
import re


def count_consecutive_duplicate(card_no):
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


def validate_input(card_no: str):
    if count_consecutive_duplicate(card_no.replace("-", "")):
        raise Exception(
            {
                "success": "False",
                "message": "More than 4 consecutive numbers are not allowed",
            }
        )
    regex = r"(^[4|5|6]\d{3})-(\d{4})-(\d{4})-(\d{4})"
    match = re.search(regex, card_no)
    if match:
        print(
            {
                "success": "Valid Card",
                "message": "Credit Card number is validated successfully",
            }
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate credit card")
    parser.add_argument(
        "card_number",
        metavar="credit card number",
        type=str,
        help="enter your credit card number",
    )
    args: str = parser.parse_args().card_number
    print(validate_input(args))
