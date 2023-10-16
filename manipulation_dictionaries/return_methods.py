print("==================================")
print("Get the value of a key with get()")
shirt = {"color": "purple", "size": "M", "price": 165.43}
print(shirt.get("color"))
print(shirt.get("size"))

print("==================================")
print("Know if a key existe")
print("price" in shirt)
print("stock" in shirt)

print("==================================")
print("Get keys and values from a dictionary with items()")
for key, value in shirt.items():
    print(key, value)

print("==================================")
print("Get keys from dictionary with keys()")
for key in shirt.keys():
    print(key)

keys = list(shirt.keys())
print(keys)

print("==================================")
print("Get values from dictionary with values()")
for value in shirt.values():
    print(value)

values = list(shirt.values())
print(values)

print("==================================")
print("Get the num of elements from dictionary with len()")
print(len(shirt))
