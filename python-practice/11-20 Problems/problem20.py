# Q20. Create a program to find the second largest number in a list.

numbers = [24, 74, 29, 82, 82, 74, 79]
largest1 = numbers[0]
largest2 = numbers[1]

for num in numbers:
    if num > largest1:
        largest2 = largest1
        largest1 = num
    elif num < largest1 and num > largest2:
        largest2 = num

print(f"The second largest number is {largest2}.")
