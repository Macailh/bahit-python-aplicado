print("==================================")
print("Count number of occurrences of a text fragment")
string1 = "Welcome to my application"
print(string1.count("e"))
print(string1.count("a"))

print("==================================")
print("Search for a text within a string using find()")
string2 = "Welcome to my application"
print(string2.find("to"))          # returns the first index where 'to' starts, if not found returns -1
print(string2.find("to", 0, 10))  # searches for 'to' between indices 0 and 10

print("==================================")
print("Search for a text within a string using index()")
# index() is similar to find() but raises a ValueError if the substring is not found
try:
    print(string2.index("to"))
    print(string2.index("to", 0, 10))
except ValueError as e:
    print(e)

print("==================================")
print("Using Regular Expressions for advanced searches")
import re
# Search for any word that starts with 'a'
matches = re.findall(r'\ba\w+', string2)
for match in matches:
    print(match)
