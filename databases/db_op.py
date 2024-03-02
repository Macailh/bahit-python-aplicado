from tabulate import tabulate

# Data for the table
data = [
    ["Open connection", "connect"],
    ["Open cursor", "cursor"],
    ["Execute query", "execute"],
    ["Commit changes", "commit"],
    ["Retrieve results (all)", "fetchall"],
    ["Close cursor (connection)", "close"],
    ["Close connection (cursor)", "close"],
]

# Print the table
print(tabulate(data, headers=["Operation", "Name in Python"], tablefmt="grid"))
