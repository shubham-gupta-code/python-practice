# Q4. Create a program that prints the multiplication table of a given number.

num = 10

i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i = i + 1   # Increases the 'i' values by 1 in every iteration - (Important)

# Here i = 1 and 'while' is a keyword for looping. It runs until the condition gets False. Condition is (i <= 10)
# In our case it is true 10 times which is need for printing a table of a number