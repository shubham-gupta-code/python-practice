# 33. Write a program to find the maximum and minimum in a list.

# With min() and max()
lst = [20, 40, 40, 30, 10, 50]
print("Using min() and max():")
print(f"The maximum value in the list is {max(lst)} and minimum is {min(lst)}.")


# Without any functions
min = lst[0]
max = lst[0]

for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]
    if lst[i] > max:
        max = lst[i]
print("\nWithout any functions:")
print(f"The maximum value in the list is {max} and minimum is {min}.")
