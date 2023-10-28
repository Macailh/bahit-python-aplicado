with open("file_management_and_manipulation/file.txt", "r") as f:
    content = f.read()
    print(content)


content = """
New content    
"""
with open("file_management_and_manipulation/file_two.txt", "w") as f:
    bytes_written = f.write(content)
    print(f"{bytes_written} bytes have been written to the file.")
