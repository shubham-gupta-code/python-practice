# Q23. Write a Python program to print a pattern of stars in a triangle.

'''
    *
   ***
  *****
 *******
*********
'''

n = int(input("Enter a number: "))

for i in range(n):
    print(" " * (n-(i+1)), end="")
    print("*" * (n+i - (n-(i+1))))

