import argparse

def group_similar_audience(text):
 transformed_list = []
 count = 1
 prev_char = text[0]

 for character in text[1:]:
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