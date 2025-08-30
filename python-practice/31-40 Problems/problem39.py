# 39. Write a function to count the frequency of elements in a list. 

lst = [20, 40, 30, 10, 50, 40, 20, 15, 18, 61, 15, 20, 35, 10]
d = {}
for num in lst:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

print(d)
