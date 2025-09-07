# Q59. Write a function to merge two dictionaries and handle key collisions by summing values.

d1 = {"apple": 3, "banana": 5, "cherry": 2}
d2 = {"banana": 4, "cherry": 6, "date": 7}

def merge_dictionaries(d1, d2):
    d3 = {}
    for key, value in d1.items():
        if key in d2:
            d3[key] = d2[key] + value
        else:
            d3[key] = value
    for key, value in d2.items():
        if key not in d3:
            d3[key] = value
    return d3

mergerd_dictionaries = merge_dictionaries(d1, d2)
print(mergerd_dictionaries)
