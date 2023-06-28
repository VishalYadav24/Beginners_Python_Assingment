import argparse
import re


def minion_game_score_counter(text):
    regex_patter = r"[A-Z]*"
    match = re.search(regex_patter, text)
    if len(match.group()) == len(text):
        consonant_score = 0
        vowel_score = 0

        for i in range(len(text)):
            if text[i] in "AIEOU":
                vowel_score += len(text[i:])
            else:
                consonant_score += len(text) - i
        if vowel_score > consonant_score:
            print(f"Kevin wins with score  of {vowel_score}")
        elif vowel_score == consonant_score:
            print(f"Draw no one wins with equal score  of {vowel_score}")
        else:
            print(f"Stuart wins with score  of {consonant_score}")
    else:
        raise ValueError("Please provide only uppercase letters")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate winner of minion game who was most substrings formed"
    )
    parser.add_argument(
        "minion_text",
        metavar="minion_text",
        type=str,
        help="Please provide text / string ",
    )
    args: str = parser.parse_args().minion_text
    minion_game_score_counter(args)
