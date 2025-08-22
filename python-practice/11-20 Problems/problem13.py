# Q13. Write a program to print all prime numbers between 1 and 1000.

for num in range(2, 1001):
    for n in range(2, int((num/2)+1)):
        if num%n==0:
            break
    else:
        print(num)
