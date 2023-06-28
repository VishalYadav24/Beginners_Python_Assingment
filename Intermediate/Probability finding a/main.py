import itertools


def find_probability(list_of_alphabets,indices) -> str :
    """
    Calculates the probability of finding alphabet "a" in the given list

    Returns:
          string denoting the probability value : (float) corrected upto 3 decimals
    """
    combinations_list = list(itertools.combinations(list_of_alphabets, indices))
    desirable_list = [pair for pair in combinations_list  if "a" in pair ]
    return (f'probability of finding "a" in  {len(combinations_list)} combinations is : {round((len(desirable_list)/len(combinations_list)),3)}')


if __name__ == "__main__":
    length_of_input : int = int(input("enter the length of list"))
    list_of_alphabets: list = input("enter list elements").split()
    indices: int = int(input("enter term upto which probability is to be calculated"))
    print(find_probability(list_of_alphabets,indices)) 