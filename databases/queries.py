import mysql.connector

# Establish connection with the database
connection = mysql.connector.connect(
    host="localhost", user="user", password="password", database="database"
)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

try:
    # Execute a select SQL query
    cursor.execute("SELECT * FROM table")

    # Get the results of the query
    results = cursor.fetchall()

    # Iterate over the results and print them
    for row in results:
        print(row)

    # Execute an insert SQL query
    cursor.execute(
        "INSERT INTO table (column1, column2) VALUES (%s, %s)", ("value1", "value2")
    )

    # Commit to confirm the changes in the database
    connection.commit()

except mysql.connector.Error as error:
    # Handle MySQL errors
    print("Error executing query:", error)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
