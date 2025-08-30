# 35. Write a function to reverse a list.

print("Reversed List:")

# Using reverse():-
lst1 = [10, 20, 30, 40, 50]
def reverse_lst(lst1):
    lst1.reverse()
    print(f"Using reverse():\n{lst1}")
reverse_lst(lst1)

# this 'reverse' method modifies/changes list and do not return anything.


# Without using any functions or methods:-
lst2 = [10, 20, 30, 40, 50]
def reverse_lst2(lst2):
    i = 0
    j = len(lst2)-1
    while i < j:
        lst2[i], lst2[j] = lst2[j], lst2[i]
        i += 1
        j -= 1

reverse_lst2(lst2)
print(f"\nWithout using reverse():\n{lst2}")
