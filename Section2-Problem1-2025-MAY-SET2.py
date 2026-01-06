def count_unique_even_odd(l: list)-> dict:
    '''Returns a dict with the count of unique even and odd numbers in the list.

    Eg. 
    >>>l = [1, 2, 2, 3, 4, 5, 5, 6]
    >>>count_unique_even_odd(l)
    {"even": 3, "odd": 3}

    Args:
        l(list)  : a list of integers.

    Returns:
        dict: a dict with the count of unique even and odd numbers in the list.
    '''
    
    
    counts = {'even':0,"odd":0}
    for num in set(l):
        if(num % 2 == 0):
            counts['even'] += 1
        else:
            counts['odd'] += 1
    return counts
    # alternate way using comprehensions
    # return {
    #   'odd': len({x for x in l if x%2!=0}),
    #   'even': len({x for x in l if x%2==0})
    # }

# #Another Method

# def count_unique_even_odd(l: list)-> dict:
      
#     setl=set(l)
#     even=0
#     odd=0
#     for i in setl:
#        if i%2==0:
#            even +=1
#        else:
#             odd +=1
#     return {"even" : even,"odd":odd}

# Counts unique even and odd numbers
# Write a function count_unique_even_odd that takes list of integers, returns a dictionary with the count of unique even and odd numbers in the list.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> l = [1, 2, 2, 3, 4, 5, 5, 6, 9]
# >>> count_unique_even_odd(l)
# {"even": 3, "odd": 4}
# Explanation

# unique even numbers are 2,4 and 6 and their count is 3
# unique odd numbers are 1,3,5 and 9 and their count is 4
    
