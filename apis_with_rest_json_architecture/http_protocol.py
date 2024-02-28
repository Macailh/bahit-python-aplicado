# Define the table as a list of tuples
table = [
    ("Method", "Description"),
    ("GET", "Retrieves any type of information."),
    (
        "HEAD",
        "Similar to GET but the server must not return a message body in the response.",
    ),
    (
        "POST",
        "While GET retrieves data from the URI, POST requests the server to accept the encapsulated information as an entity within the request itself.",
    ),
    (
        "PUT",
        "While POST is limited to sending encapsulated information, PUT adds to the request that the sent information (encapsulated as in POST) be stored in the resource being requested. If the requested resource exists, HTTP interprets that it should be modified with the new received entity. If it does not exist, it could create the new entity (provided the resource has the ability to do so).",
    ),
    ("DELETE", "Requests the server to delete the resource identified in the URI."),
]

# Print the table
for row in table:
    print("{:<10} {:<}".format(row[0], row[1]))

print(
    "======================================================================================================================================"
)

code_description = {
    "1xx": "Information - The request has been received and the process continues",
    "2xx": "Success - The request was received and executed successfully",
    "3xx": "Moved - The request requires additional actions to be completed",
    "4xx": "Client Error - The request was either incomplete or contained format errors",
    "5xx": "Server Error - The request could not be completed due to a server error",
}

# Print each key-value pair in the dictionary
for code, description in code_description.items():
    print(f"Class {code}: {description}")

print(
    "======================================================================================================================================"
)

code_description_detail = {
    "200": "OK - The request was successful",
    "301": "Moved Permanently - The requested resource has been permanently moved and assigned a new URI",
    "304": "Not Modified - When a new request is made using the GET method and the resource has not changed since the last query by the same client, the server should respond with this code instead of '200 OK'",
    "307": "Temporary Redirect - Temporary redirection to a new resource (with new temporarily assigned URI)",
    "400": "Bad Request - The request was not understood by the server",
    "403": "Forbidden - The request has been rejected by the server even though it was understood and should not be retried",
    "404": "Not Found - The server could not find the requested resource",
    "405": "Method Not Allowed - The method of the request does not match the method(s) required by the resource",
    "408": "Request Timeout - The client's request took longer than the server can wait",
    "500": "Internal Server Error - The server encountered an internal problem and had to abruptly terminate the request",
    "503": "Service Unavailable - The server is temporarily unavailable to handle the request",
}

# Print each key-value pair in the dictionary
for code, description in code_description_detail.items():
    print(f"Code {code}: {description}")
