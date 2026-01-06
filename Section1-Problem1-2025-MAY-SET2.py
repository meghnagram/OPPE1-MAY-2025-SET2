
def is_even_or_divisible_by_5(num:int) -> bool:
    '''
    Given an integer, check if a number is either even or divisible by 5.

    Eg. 
    is_even_or_divisible_by_5(8) -> True
    is_even_or_divisible_by_5(10) -> True
    is_even_or_divisible_by_5(15) -> True
    is_even_or_divisible_by_5(7) -> False

    Args:
        num (int) : An integer.

    Returns:
        bool: True if even or if divisible by 5 else False.
    '''
    
    return (num % 2 == 0) or (num % 5 == 0)

# #Another Method


# def is_even_or_divisible_by_5(num:int) -> bool:
#     if num%5==0 or num%2==0:
#         return True
#     else:
#         return False

# Check is even or divisible by 5
# Write a function is_even_or_divisible_by_5 that takes an integer as input and return True if it is even or is divisible by 5 else False.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example is_even_or_divisible_by_5(8) -> True (8 is even number) is_even_or_divisible_by_5(10) -> True (10 is even number and divisible by 5) is_even_or_divisible_by_5(15) -> True (15 is divisible by 5) is_even_or_divisible_by_5(7) -> False (not an even number nor divisible by 5)
    
