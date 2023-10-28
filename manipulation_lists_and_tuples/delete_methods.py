print("==================================")
print("Delete the last element from a list with pop()")
male_names = ["Alfredo", "Alvaro", "Daniel", "Miguel"]
print(male_names.pop())
print(male_names)

print("==================================")
print("Delete a exact element with the index with pop(index)")
male_names.pop(1)
print(male_names)

print("==================================")
print("Delete a exact element with the value with remove()")
male_names.remove("Alfredo")
print(male_names)
