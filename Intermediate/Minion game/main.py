import argparse
import re


def minion_game_score_counter(text: str) -> str:
    """
    Calculate the minion game score by comparing word formed using vowels and consonants, and return winner

    Arguments:
        text: string  user provided text (upper case)

    Returns:
        message: string - containing winner and its score
    """
    regex_patter = r"[A-Z]*"
    match = re.search(regex_patter, text)
   
    if len(match.group()) == len(text):
        consonant_score: int = 0
        vowel_score: int = 0

        for i in range(len(text)):
            if text[i] in "AIEOU":
                # slicing the list with current value of i and taking its length = no of word which can be formed
                vowel_score += len(text[i:])
            else:
                consonant_score += len(text) - i
        if vowel_score > consonant_score:
            return f"Kevin wins with score  of {vowel_score}"
        elif vowel_score == consonant_score:
            return f"Draw no one wins with equal score  of {vowel_score}"
        else:
            return f"Stuart wins with score  of {consonant_score}"
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
    print(minion_game_score_counter(args))
