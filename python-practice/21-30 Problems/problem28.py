# Q28. Write a program to find the sum of all even numbers in a list.

even_numbers = [28, 10, 92, 62, 94, 30, 28, 36, 92, 56, 10]

sum_of_even_numbers = 0
for num in even_numbers:
    sum_of_even_numbers += num

print(f"The sum of all the even numbers is {sum_of_even_numbers}.")
