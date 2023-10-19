from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.
    Args:
        int_list: A list of integer.
    Returns:
        A list of even integers.
    """
    # TODO: Implement even_list
    pass

# sum_of_squares_of_even function
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum_number = 0
    for item in even_int_list:
        sum_number += item * item
    return sum_number

# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)
    
# Boilerplate code
if __name__ == "__main__":
    main()