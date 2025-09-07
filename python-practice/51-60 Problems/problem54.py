# Q54. Write a function to flatten a nested list.

nes_lst = [[1, 2], [3, 4], [5, 6, 7], [8, 9]]
flattened = [item for lst in nes_lst for item in lst]
print(flattened)


# For deeply nested lists
deeply_nested_list = [1, 2, [3, 4], 5, [6, [7, [8], 9, 10], 11]]

def flatten_lists(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):  # Checking, Is a item belongs to a particular class
            flattened.extend(flatten_lists(item))  # Extending the list by appending any number of elements
        else:
            flattened.append(item)
    return flattened

flattened_list = a = flatten_lists(deeply_nested_list)
print(flattened_list)

