# Q9. Write a Python script to reverse a given string.

given_string = "abcd"
reversed_string = ""

for char in reversed(given_string):
    reversed_string = reversed_string + char

print(f"Reversed string --> {reversed_string}")


# reversed() is used to loop through a string but from last character to start character
# In our case 'char' variable in for loop takes a character from 'given_string' in a reversed order with the help of reversed()
