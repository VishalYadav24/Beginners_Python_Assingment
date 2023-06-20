import argparse


def filter_duplicate_list(text_with_redundancy: str)-> list:
    """ Convert a list of of duplicate elements to list of unique elements.
        
        Arguments:
            text_with_redundancy (str): The text of duplicate elements provided by user
        Returns:
           list -> list of unique elements    
    """
    # converting user text to list
    list_with_redundancy = list(text_with_redundancy)
    temp_list = []
    for element in list_with_redundancy:
        if element not in temp_list:
            temp_list.append(element)
    return temp_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare fresh list with no redundancy from user provided list containing duplicates"
    )
    parser.add_argument(
        "redundant_list",
        metavar="redundant_list",
        type=str,
        help="Please provide text / string  containing duplicate elements",
    )
    args: str = parser.parse_args().redundant_list
    print(filter_duplicate_list(args))
