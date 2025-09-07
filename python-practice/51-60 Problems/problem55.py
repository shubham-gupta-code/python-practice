# Q55. Write a function to find the second highest number in a list.

lst = [3, 5, 9, 2, 8, 3, 8, 0, 4, 9]

def second_highest(lst):
    largest = lst[0]
    second_largest = lst[1]
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest

second_highest = second_highest(lst)
print(second_highest)
