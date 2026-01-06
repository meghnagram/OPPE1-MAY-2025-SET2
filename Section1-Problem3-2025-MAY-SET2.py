def make_dict_from_elems_in_index(keys, values, index:int)-> dict:
    '''
    Returns a dictionary with one key and value pair
    taken from the given index of keys and values list.

    Eg:
    >>> keys = ['apple', 'banana', 'cherry']
    >>> values = [10, 20, 30, 40]
    >>> make_dict_from_elems_in_index(keys, values, 1) 
    {'banana': 20}
    >>> make_dict_from_elems_in_index(keys, values, -1) 
    {'cherry': 40}

    Args:
        keys (list): The list with the keys.
        values (list): The list with the values.
        index (int): An integer

    Returns:
        dict: Dictionary with only one key-value pair, where the key and value are taken from the given index.
    '''
 
    return {keys[index]:values[index]}

# #Another Method
# def make_dict_from_elems_in_index(keys, values, index:int)-> dict:
#     a=keys[index]
#     b=values[index]
    
#     d={}
#     d[a]=b 
#     return d

# Make dictionary from elements in index of lists
# Write a function make_dict_from_elems_in_index that returns a dictionary consisting of a single key-value pair formed as follows:

# the key is the element at the given index from the list keys.
# the value is the element at the given index from the list values .
# Assume the index is always within valid bounds for both lists.

# Example

# >>> keys = ['apple', 'banana', 'cherry']
# >>> values = [10, 20, 30, 40]
# >>> make_dict_from_elems_in_index(keys, values, 1) 
# {'banana': 20}
# >>> make_dict_from_elems_in_index(keys, values, -1) 
# {'cherry': 40}
# Explanation

# Elements of keys, values at index 1 are banana, 20 respectively. Hence the dictionary is {'banana': 20}
# Elements of keys, values at index -1 are cherry, 40 respectively. Hence the dictionary is {'cherry': 40}
