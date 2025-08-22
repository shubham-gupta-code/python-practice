# Q16. Write a program to find the GCD/HCF of two numbers.

a = 38
a_factors = [a]   # 38 is already the factor of 38

b = 19
b_factors = [b]   # 19 is already the factor of 19

for n in range(1, int(a/2)+1):
    if a%n==0:
        a_factors.append(n)
        
for n in range(1, int(b/2)+1):
    if b%n==0:
        b_factors.append(n)

a_factors = set(a_factors)   # Convert list into set for intersection operation
b_factors = set(b_factors)

common_factors = a_factors.intersection(b_factors)   # intersection() is used to get common elements between two sets

print(f"The GCD/HCF of {a} and {b} is {max(common_factors)}.")
