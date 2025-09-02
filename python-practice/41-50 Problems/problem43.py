# 43. Create a set and perform union, intersection, and difference.

s1 = {1, 3, 5, 6, 7, 9, 10, 11}
s2 = {2, 4, 6, 8, 10, 12}

set_union = s1.union(s2)  # all elements without repetition
set_intersection = s1.intersection(s2)  # common elements
set_difference = s1.difference(s2)  # s1 - s2

print(f"Union: {set_union}")
print(f"Intersection: {set_intersection}")
print(f"Difference: {set_difference}")
