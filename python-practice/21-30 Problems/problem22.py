# Q22. Create a program to print all Armstrong numbers between 1 to 1000.

for num in range(1, 1001):
    digits = str(num)
    exponent = len(digits)

    total_sum = 0
    for d in digits:
        total_sum += int(d)**exponent
        
    if num == total_sum:
        print(num)

