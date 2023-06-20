def fibonacci_series() -> None:
    """" Print fibonacci series upto the user specified terms (int)
    """
    count: int = 0
    first_term: int = 0
    second_term = 1
    next_term: int = 0
    sequence_list:list[int] = [first_term, second_term]
    number_of_terms = int(
        input("Enter a number of terms upto which fibonacci series will be printed")
    )
    if number_of_terms > 0:
        while count < number_of_terms:
            first_term = second_term
            second_term = next_term
            next_term = first_term + second_term
            sequence_list.append(next_term)
            count += 1
        print("Your fibonacci series is like this:", sequence_list)
    elif number_of_terms == 0:
        print("Your fibonacci series is like this:", first_term)
    else:
        print("Enter positive number")


if __name__ == "__main__":
    fibonacci_series()
