from json import loads, dumps


json_books = """
    {
        "Under the dome": {
            "ISBN": "978-3-16-148410-0",
            "author": "Stephen King",
            "year": 2009,
            "publisher": "Scribner",
            "genre": "Science fiction",
            "price": 30.00,
            "currency": "USD",
            "pages": 1074,
            "language": "English",
            "cover": "Hardcover",
            "dimensions": {
                "height": 23.5,
                "width": 16.5,
                "depth": 5.5
            }
        }
    }
"""

print("================Books================")
print("=====================================")
print("Dict of books")
dict_books = loads(json_books)
print(dict_books)
print(type(dict_books))
print("=====================================")
print("JSON books")
json_books2 = dumps(dict_books, indent=4)
print(json_books2)
print(type(json_books2))
print("=====================================")
