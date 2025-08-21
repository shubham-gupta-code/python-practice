# Q10. Check if a number is a palindrome.

# 121 --> 121 (Palindrome ✅)
# 13231 --> 13231 (Palindrome ✅)
# 3992 --> 2993 (Palindrome ❌)

number = 121

number = str(number)   # convert into str datatype (121 --> '121')

list_of_numbers = list(number)   # str to list datatype ('121' --> ['1', '2', '3'])
                                              # Indexes/positions =  0    1    2

i = 0   # pointing to 1st number of list (index = 0)
j = len(i)-1   # pointing to last number of list (index = 2)

while i<j:
    if list_of_numbers[i] != list_of_numbers[j]:
        print(f"{number} is not Palindrome number.")
        break
    i = i + 1
    j = j - 1
else:
    print(f"{number} is a Palindrome number.")

print(list_of_numbers)


# lists and strings have indexes or positions of every value
# len() is used to get length of a list or string e.g:- lst = ['a', 'b', 'c', 'd'], then len(lst) --> 4
# In our case I am putting 'i' to first place and 'j' to last place of the list
# In the while statement we are checking if 'i' not equals to 'j' means it is not a palindrome
# 'break' keyword is used to stop the loop immediately and get outside of the loop
# we can use else with loops, else is only executed when while loop executed without break

# Illustration:- ['1', '2', '1']
#                  i         j
#                if value of i is equal to j then change the position of i and j

#                ['1', '2', '1']
#                      i,j

#                 here i<j becomes False and else block executed because no break happened in while loop

