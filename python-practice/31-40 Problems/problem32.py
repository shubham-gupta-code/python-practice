# Q32. Create a list and find the sum of all its elements.

# With 'sum()'
lst = [20, 40, 30, 10, 50]
print(f"The sum of all elements using sum() is {sum(lst)}.")

# Without any functions
total_sum = 0
for num in lst:
    total_sum += num
print(f"The sum of all elements without any function is {total_sum}.")
