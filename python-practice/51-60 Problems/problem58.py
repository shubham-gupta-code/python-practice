# Q58. Write a program to remove all None values from a list.

lst = [None, 48, 29, None, "abc", True, None, 30.20, False, "xyz", None]

new_list = [num for num in lst if num != None]

print(new_list)
