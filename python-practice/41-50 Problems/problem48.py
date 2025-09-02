# 48. Create a dictionary and iterate over its keys and values.

my_dictionary = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
    "date": 4,
    "elderberry": 5,
    "fig": 6,
    "grape": 7,
    "honeydew": 8,
    "kiwi": 9,
    "lemon": 10
}

for fruit_name, fruit_value in my_dictionary.items():
    print(f"{fruit_name} --> {fruit_value}")

# items() is used to get key and value of dictionary.
print(my_dictionary.items())
