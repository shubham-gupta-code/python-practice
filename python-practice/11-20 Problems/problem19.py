# Q19. Write a program to calculate the sum of digits of a number and also multiplication of digits.

numbers = 52314
sum_of_digits = 0
multiplication_of_digits = 1

numbers = str(numbers)

for num in numbers:
    sum_of_digits += int(num)
    multiplication_of_digits *= int(num)

print(f"The sum of all digits of number {numbers} is {sum_of_digits}.")
print(f"The multiplication of all digits of number {numbers} is {multiplication_of_digits}.")
