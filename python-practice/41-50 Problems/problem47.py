# 47. Write a function to count vowels in a string.

VOWELS = ['a', 'e', 'i', 'o', 'u']

string_to_check = input("Write something here: ")

def count_vowels(string):
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1
    return count

no_of_vowels = count_vowels(string_to_check)
print(f"The number of vowels in '{string_to_check}' is {no_of_vowels}.")
