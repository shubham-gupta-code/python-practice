# Q18. Check whether a character is a vowel or consonant.

character = input("Type a single character: ").lower()   # lower() converts the string in lowercase
vowels = ['a', 'e', 'i', 'o', 'u']

print(f"{character} is a vowel.") if character in vowels else print(f"{character} is a consonant.")
# This is a inline or oneline if-else statement in python

# Syntax: (value_if_true) if (condition) else (value_if_false)
