# Q57. Write a function to find the missing number from a list of N to N numbers.

lst = [7, 8, 9, 10, 11, 13, 14, 15, 16]

def find_missing_number(lst):
    start_num = lst[0]
    for num in lst[1:]:
        if num == start_num+1:
            start_num += 1
        else:
            return start_num+1

missing_number = find_missing_number(lst)    
print(f"Missing Number is {missing_number}.")
