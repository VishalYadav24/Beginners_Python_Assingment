import re


def restructure_list() -> None:
    """ Print a new list of square from  elements of  user provided list
    """
    try:
        original_list:str = input("Enter text of numbers only:")
        if int(original_list):
            list_with_squares:list[int] = list(map(lambda x: int(x) ** 2, list(original_list)))
            print(list_with_squares)
    except ValueError as e:
        print(e, "Please provide a series of numbers")


if __name__ == "__main__":
    restructure_list()
