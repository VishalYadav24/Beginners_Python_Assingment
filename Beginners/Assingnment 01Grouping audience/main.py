import argparse

def group_similar_audience(sitting_order_text: str) -> list[str]:
 """
  Groups similar alphabets (denotes audience sitting order) and their count depending on the position they appear on original text given by user.

  Arguments:
    sitting_order_text : string -> represents sitting order of audience

    Returns:
      list[str] -> list -> list of similar alphabets along with count of occurrence (denotes audience sitting order)  
 """
 transformed_list: list = []
 count: int = 1
 prev_char: str = sitting_order_text[0]

 for character in sitting_order_text[1:]:
    if character == prev_char:
       count += 1
    else:
       transformed_list.append((prev_char,count))
       count = 1
       prev_char = character
 # adding last element to transformed_list      
 transformed_list.append((prev_char,count))      
 return transformed_list     




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare list of grouping from string containing audience sitting oder"
    )
    parser.add_argument(
        "audience_sitting_order",
        metavar="audience_sitting_order",
        type=str,
        help="Please provide text / string  containing audience sitting oder",
    )
    args: str = parser.parse_args().audience_sitting_order
    print(group_similar_audience(args))