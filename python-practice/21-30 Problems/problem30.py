# Q30. Write a program to display the cube of the number up to an integer.

number = int(input("Enter a number: "))

for num in range(1, number+1):
    print(f"Cube of {num} = {num**3}.")
