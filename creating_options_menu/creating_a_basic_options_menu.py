print("=============================")
print("Search pattern in file with search()")


def read_file():
    """Read CSV file"""
    return "read"


def write_file():
    """Write CSV file"""
    return "write"


def _add_numbers(list):
    """Add the numbers in a list"""
    return "private"


functions = [read_file, write_file, _add_numbers]

num = 1
menu = "Choose an option: \n"
for function in functions:
    menu += "\t{}. {}\n".format(num, function.__doc__)  # Access the docstring directly from the function
    num += 1

print(menu)
option = int(input("Your option: "))

function = functions[option - 1]

function()
