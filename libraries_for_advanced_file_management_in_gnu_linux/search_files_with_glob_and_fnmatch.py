import glob
import fnmatch

# Use glob to find files ending in '.txt'
txt_files = glob.glob('*.txt')

# Use fnmatch to further filter this list, looking for files that start with 'example'
example_files = [file for file in txt_files if fnmatch.fnmatch(file, 'example*')]

print(example_files)
