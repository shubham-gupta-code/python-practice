# Q26. Convert a decimal number to binary using loops. 

number = int(input("Enter a number: "))

if number == 0:
    print(f"The binary number of 0: 0")

else:
    binary_values = []
    quotient = number

    while quotient > 0:
        binary_values.append(quotient%2)
        quotient //= 2   # integer division

    binary_values.reverse()
    binary_values = "".join(map(str, binary_values))

    print(f"The binary number of {number}: {binary_values}")
