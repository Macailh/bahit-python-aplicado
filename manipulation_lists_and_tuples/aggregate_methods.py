print("==================================")
print("Add element to end of list with append()")
male_names = ["Alfredo", "Alvaro", "Daniel", "Miguel"]
male_names.append("Jose")
print(male_names)

print("==================================")
print("Add elements to end of list with extend()")
male_names.extend(["Eduardo", "Gerardo"])
print(male_names)

print("==================================")
print("Add element in exact position with insert()")
male_names.insert(0, "Rick")
print(male_names)
male_names.insert(3, "Angel")
print(male_names)
print(male_names[3])
