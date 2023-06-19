import argparse
import re
def sort_alphanumeric_string(alphanumeric_text:str):
 """ Sort a given alphanumeric string in to list of strings following below pattern
       - small case alphabets comes first
       - large case alphabets comes second
       - odd numbers come third
       - even numbers come at last

     Arguments: alphanumeric_text - string to sort given by user

     Returns:
       List of sorted strings 
 """
 small_case_list = []
 upper_case_list = []
 numeric_case_list = []
 regex_small_case = r'[a-z]'
 regex_upper_case = r'[A-Z]'
 regex_numeric_case = r'[0-9]'
 for characters in alphanumeric_text:
    if re.findall(regex_small_case,characters):
     small_case_list.append(characters)
    if re.findall(regex_upper_case,characters):
     upper_case_list.append(characters)
    if re.findall(regex_numeric_case,characters):
     numeric_case_list.append(characters)
 even_numbers_list = list(filter(lambda x : int(x)%2 == 0,numeric_case_list))
 odd_numbers_list = list(filter(lambda x : int(x)%2 != 0,numeric_case_list))
 small_case_list.sort()
 upper_case_list.sort()
 even_numbers_list.sort()
 odd_numbers_list.sort()
 
 result = small_case_list+upper_case_list+odd_numbers_list+even_numbers_list
 return result

 



if __name__ == "__main__":
 parser = argparse.ArgumentParser(description="Sort a provided alphanumeric string")
 parser.add_argument('alphanumeric_text',metavar='alphanumeric string',type=str,help='enter alphanumeric_text made of alphanumeric characters')
 args:str = parser.parse_args().alphanumeric_text
 print(sort_alphanumeric_string(args))