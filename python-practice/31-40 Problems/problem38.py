# 38. Write a program to merge two dictionaries.

d1 = {"name": "abc",
      "age": 26,
      "profession": "SWE"}

d2 = {"salary": 90000,
      "country": "India"}

for key, value in d2.items():
    d1[key] = value

print(d1)


# Easy way to merge:-
merged_dict = d1 | d2
print(merged_dict)
