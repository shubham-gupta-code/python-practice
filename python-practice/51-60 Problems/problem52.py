# Q52. Write a function to check if a string is an anagram.

user_input = input("Enter a string: ").lower().strip()

def check_anagram(text):
    reversed_text = ""
    for char in reversed(text):
        reversed_text += char

    if text == reversed_text:
        return True

result = "It is Anagram" if check_anagram(user_input) == True else "It is not Anagram"
print(result)
