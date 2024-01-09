from zipfile import ZipFile

# Writing zip files
with ZipFile("folder/file.zip", "w") as z:
    z.write("foo.txt")
    z.write("bar.txt")
    z.write("baz.txt")

# Reading zip files
with ZipFile("folder/file.zip", "r") as z:
    z.extractall("destination/folder", pwd="key") # pwd param is optional