# Unzip files
from tarfile import open as tar_open

with tar_open("example.tar.bz2", "r:bz2") as tar:
    tar.extractall("destination/folder")

# Compress files
with tar_open("folder/destination.tar.gz", "w:gz") as tar:
    tar.add("foo.txt")
    tar.add("bar.txt")
    tar.add("baz.txt")
