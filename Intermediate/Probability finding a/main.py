import itertools


def find_probability() -> str :
    """
    Calculates the probability of finding alphabet "a" in the given list

    Returns:
          string denoting the probability value : (float) corrected upto 3 decimals
    """
    length_of_input : int = int(input())
    list_of_alphabets: list = input().split()
    indices: int = int(input())
    combinations_list = list(itertools.combinations(list_of_alphabets, indices))
    desirable_list = [pair for pair in combinations_list  if "a" in pair ]
    return (f'probability of finding "a" in  {len(combinations_list)} combinations is : {round((len(desirable_list)/len(combinations_list)),3)}')


if __name__ == "__main__":
   print(find_probability())