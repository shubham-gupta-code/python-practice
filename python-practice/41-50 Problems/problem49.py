# 49. Write a function to remove all punctuation from a string.

import string
PUNCTUATION = [punc for punc in string.punctuation]  # List Comprehension (short way to create a list)

user_input = input("Type here something and I'll remove punctuation from it: ").strip()

def remove_punctuation(user_input):
    for punc in PUNCTUATION:
        user_input = user_input.replace(punc, "")
    return user_input

removed_punctuation = remove_punctuation(user_input)
print(removed_punctuation)


# string is a python built-in module which provides alphabets, punctuation and more.