print("==================================")
print("Count the number of occurrences of a certain element")
male_names = ["Juan", "Pedro", "Luis", "Angel", "Carlos", "Juan"]
print(male_names.count("Juan"))
male_names.append("Juan")
print(male_names.count("Juan"))

print("==================================")
print("Get index number")
print(male_names.index("Juan"))
print(male_names.index("Angel"))
print(male_names.index("Juan", 1, 6))
