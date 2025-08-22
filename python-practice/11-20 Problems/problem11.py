# Q11. Write a program to find the sum of first N natural numbers.

number = int(input("Enter a number: "))
total_sum = 0

for num in range(1, number+1):
    total_sum += num   # It is same as (total_sum = total_sum + num)

print(f"The sum of {number} natural integers is {total_sum}.")

