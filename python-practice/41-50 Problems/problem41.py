# 41. Write a program to sort a list in ascending order.

lst = [10, 30, 50, 5, 40, 30, 20]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[j] < lst[i]:
            lst[i], lst[j] = lst[j], lst[i]
        
print(f"The sorted list: {lst}")


# Using sort():-
lst2 = [10, 30, 50, 5, 40, 30, 20]
lst2.sort()
print(f"The sorted list using sort(): {lst}")
