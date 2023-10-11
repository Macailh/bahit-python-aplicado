print("==================================")
print("Join strings iteratively using join()")
list_of_words = ["Hello", "world", "this", "is", "a", "test"]
joined_string = " ".join(list_of_words)
print(joined_string)  # Output: Hello world this is a test

print("==================================")
print("Partition a string into three parts using a separator")
string_to_partition = "apple,banana,cherry"
partitioned_string = string_to_partition.partition(",")
print(partitioned_string)  # Output: ('apple', ',', 'banana,cherry')

print("==================================")
print("Split a string into multiple parts using a separator")
string_to_split = "apple,banana,cherry,grape"
split_string = string_to_split.split(",")
print(split_string)  # Output: ['apple', 'banana', 'cherry', 'grape']

print("==================================")
print("Split a string into lines using splitlines()")
multiline_string = """This is line one.
This is line two.
This is line three."""
lines = multiline_string.splitlines()
for line in lines:
    print(line)
