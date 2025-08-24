# Q24. Create a calculator app using if-else.

OPERATORS = ['+', '-', '*', '/']   # Variables in uppercase is considered as Constant in Python.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter Operation: ")

if operator in OPERATORS:
    if operator == '+':
        print(f"The sum of {number1} and {number2} = {number1 + number2}")
    elif operator == '-':
        print(f"The subtraction of {number1} and {number2} = {number1 - number2}")
    elif operator == '*':
        print(f"The multiplication of {number1} and {number2} = {number1 * number2}")
    elif operator == '/':
        print(f"The division of {number1} and {number2} = {number1 / number2}")

else:
    print("Please enter a valid operator.")


# Now using eval() function create calculator.

equation = str(number1) + str(operator) + str(number2)
print(f"The answer using eval() is {eval(equation)}.")
