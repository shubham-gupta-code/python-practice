# Q31. Write a function to check if a number is even or odd.

number = int(input("Enter a number: "))
def even_or_odd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"

result = even_or_odd(number)
print(result)


# def :- It is used to define a function. Function consist some number of codes that is executed when function is called by its name.

# even_or_odd(number) :- 'even_or_odd' is function name and 'number' is a parameter which is simply a variable name and this variable contain a value of any data type and then that variable used in the function

# return :- It is used to take a value from a function of any data type and then used outside the function, like in our example result consists whether 'Even' or 'Odd' as a string and also when return keyword is executed the function is exit like a 'break' in loops.
