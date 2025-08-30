# 34. Create a program that removes duplicates from a list.

print("List without duplicates:")

# Using set():-
lst = [20, 40, 30, 10, 50, 40, 20, 15, 18, 61, 15, 20, 35, 10]
no_duplicates = list(set(lst))
print(f"Using set():\n{no_duplicates}")

# set :- It is a data type in python like a list but a 'set' do not contain duplicate values and it is unordered

# Without using any functions:-
new_lst = []
for num in lst:
    if num not in new_lst:
        new_lst.append(num)

print(f"\nWithout using any functions:\n{new_lst}")
