from tabulate import tabulate

# Data for the table
data = [
    ["Create database", "CREATE DATABASE <name>;"],
    ["View all databases", "SHOW DATABASES;"],
    ["Drop database", "DROP DATABASE <name>;"],
    ["Choose a database", "USE <name>"],
    [
        "Create a table with InnoDB engine",
        "CREATE TABLE <name> ( <field1> <characteristics1>, <fieldn> <characteristicsn> ) ENGINE=InnoDB;",
    ],
    ["View all tables in a database", "SHOW TABLES;"],
    ["View structure of a table", "DESCRIBE <table>;"],
    ["Drop a table", "DROP TABLE <name>;"],
    ["Create user", "CREATE USER <name>"],
]

# Print the table
print(tabulate(data, headers=["Objective", "Statement"], tablefmt="grid"))
