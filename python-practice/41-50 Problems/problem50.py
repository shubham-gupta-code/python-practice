# 50. Write a function to capitalize the first letter of each word in a string.

import string
ALPHABETS = [alphabet for alphabet in string.ascii_letters]

user_input = input("Write a paragraph and I'll capitalize each word: ").strip()
chars = list(user_input)
chars[0] = chars[0].upper()

def capitalize_first_letter(chars):
    for i in range(1, len(chars)):
        if chars[i] == " ":
            for j in range(i+1, len(chars)):
                if chars[j] in ALPHABETS:
                    chars[j] = chars[j].upper()
                    break
    return "".join(chars)

sentence = capitalize_first_letter(chars)
print(sentence)


# Easy and More Pythonic Way to do:-
capitalized_words = " ".join(word.capitalize() for word in user_input.split())  # this is decorators
print(capitalized_words)
