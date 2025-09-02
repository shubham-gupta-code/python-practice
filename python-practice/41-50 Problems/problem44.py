# 44. Write a function to find common elements in two lists.

lst1 = [1, 3, 5, 6, 7, 9, 10, 11]
lst2 = [2, 4, 6, 8, 10, 12]

def find_common_elements(lst1, lst2):
    for num in lst1:
        if num in lst2:
            print(f"{num} ", end="")

find_common_elements(lst1, lst2)


# end="" --> It is used to avoid to go on next line for next print statement
