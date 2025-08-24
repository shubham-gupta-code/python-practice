# Q29. Create a program to check whether a number is prime or not.

number = int(input("Enter a number: "))

if number > 1:
    if number == 2:
        print("Prime")
    elif number%2==0:
        print("Not Prime")
    else:
        for num in range(3, int(number**0.5) + 1, 2):  # Check only odd numbers
            if number%num==0:
                print("Not Prime")
                break
        else:
            print("Prime")
        
else:
    print("Please enter a number greater than 1.")

