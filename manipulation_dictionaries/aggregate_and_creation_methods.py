print("==================================")
print("Copy a dictionary with copy()")
ex_dictionary = {"color": "purple", "size": "M", "price": 165.43}
shirt = ex_dictionary.copy()
print(shirt)
new_dictionary = ex_dictionary
print(new_dictionary)
new_dictionary.clear()
print(ex_dictionary)

print("==================================")
print("Create a dictionary from keys of a sequence with dict.fromkeys")
sequence = ["color", "size", "brand"]
dictionary_one = dict.fromkeys(sequence)
print(dictionary_one)

print("==================================")
print("Concatenate dictionaries with update()")
dictionary_one = {"color": "green", "price": 34}
dictionary_two = {"size": "M", "brand": "alfabhet"}
dictionary_one.update(dictionary_two)
print(dictionary_one)

print("==================================")
print("Set default value with setdefault()")
shirt = {"color": "green", "brand": "chetto"}
key = shirt.setdefault("talle", "M")
print(shirt)
shirt_two = shirt.copy()
print(shirt_two)
