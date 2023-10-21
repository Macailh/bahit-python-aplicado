from re import search

print("=============================")
print("Search pattern in string with search()")
string = "hello world"
ser = search("o\sw", string)
print(ser.group(0))

print("=============================")
print("Search pattern in file with search()")
with open("regular_expressions/auth.log", "r") as f:
    log = f.read()

regex = r".+FAILED su for root by [a-z]+\s*$"

ser = search(regex, log)

if ser:
    print(ser.group(0))
else:
    print("No matches found")
