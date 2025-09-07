# Q60. Create a function to find unique elements present in only one of two lists.

l1 = [3, 5, 7, 9, 11, 13, 10, 5, 17, 9]
l2 = [2, 3, 6, 7, 10, 11, 14, 17, 20, 22]

def unique_elements(l1, l2):
    l3 = []
    l3 = [num for num in set(l1) ^ set(l2)]   # ^ is used to get the data which belongs to only one set
    return l3

result = unique_elements(l1, l2)
print(result)
