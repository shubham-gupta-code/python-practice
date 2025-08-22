# Q15. Create a program to print the Fibonacci series up to N terms.
# Fibonacci series looks like this 0 1 1 2 3 5 8 13 21 34 ...

number = int(input("Enter a number: "))
a = 0
b = 1

if number >= 1:
    if number == 1:
        print(a)
    elif number == 2:
        print(f"{a}\n{b}")
    else:
        print(f"{a}\n{b}")
        for _ in range(3, number+1):
            c = a+b
            a, b = b, c
            print(c)


# Why '_' is used in for loop: If you don't need the value of the loop variable, But you care about repating something a number of times, Like in our case we have to iterate some number of times and not using the value of loop variable in the loop.
