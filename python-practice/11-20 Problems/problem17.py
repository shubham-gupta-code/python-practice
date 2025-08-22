# Q17. Write a program to find the LCM of two numbers.

a = 6
a_multiples = []

b = 4
b_multiples = []

for i in range(1, 11):
    a_multiples.append(a*i)
    b_multiples.append(b*i)

a_multiples, b_multiples = set(a_multiples), set(b_multiples)

common_multiples = a_multiples.intersection(b_multiples)

print(f"The LCM of {a} and {b} is {min(common_multiples)}.")
