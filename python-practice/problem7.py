# Q7. Write a program to calculate the factorial of a number using a loop.

user_input = int(input("Enter a number: "))
factorial = 1

for i in range(1, user_input+1):
    factorial = factorial * i # reassigning factorial value by multiplying it with value of 'i'

# for keyword is used to loop over a list, strings, dictionaries, and other data types and also to loop through a range of number, like in our case we did.

# range() is used to go through 0 or starting given number to a given number - 1
# e.g:- range(2, 7) --> 2,3,4,5,6
# In our case it will start from 1 and go until user_input value because we add 1
# So, if user type 5 then range(1, 5+1) it will be like 1,2,3,4,5

print(f"The factorial of {user_input} is {factorial}.")
