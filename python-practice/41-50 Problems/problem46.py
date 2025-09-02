# 46. Create a function that checks whether a string is a palindrome.

word = input("Type a word: ").lower().strip()

def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

answer = is_palindrome(word)
if answer == True:
    print(f"Yes, the word {word} is palindrome.")
else:
    print(f"No, the word {word} is not palindrome.")

# lower() is used to convert all the character of a string into lowercase.
# strip() is used to remove right and left spaces of a string.
