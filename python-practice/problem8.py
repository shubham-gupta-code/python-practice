# Q8. Create a program to count the number of vowels in a string.

user_input = input("Write a word or sentence: ")
vowels = ['a', 'e', 'i', 'o', 'u']   # To store more than one value in a variable, Then "list" come to use. Initialized with "[]"
count_vowels = 0

for i in user_input:   # Looping through the strings, each time a strings character store in i variable
    if i in vowels:   # 'in' is used to check, is a value(i) exists in the given list of values(vowels)
        count_vowels = count_vowels + 1   # Increases the count value by 1, when a vowel is found in a string

print(f"The string you typed, have {count_vowels} times vowels.")
