import re
def restructure_list():
    try:
        original_list = input("Enter text of numbers only:")
        if (int(original_list)):
            list_with_squares = list(map(lambda x: int(x)**2, list(original_list)))
            print(list_with_squares)
    except ValueError as e:
        print(e,"Please provide a series of numbers")


if __name__ == "__main__":
   restructure_list()