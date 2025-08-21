# Q5. Write a program to find the largest of three numbers.

a = 9
b = 15
c = 15

if a>b and a>c:
    print("a is largest number.")
elif b>a and b>c:   # 'elif' is used to to run a block of code if condition is True otherwise it will not run
    print("b is largest number.")
else:
    print("c is largest number.")

# 'and' checks that all the different given conditions should be True. Then executes the given code. 