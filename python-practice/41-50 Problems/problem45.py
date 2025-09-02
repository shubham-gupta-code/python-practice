# 45. Write a function that returns the factorial of a number. 

number = int(input("Enter a number: "))

def fact_of(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

factorial = fact_of(number)
print(f"The factorial of {number} is {factorial}.")
