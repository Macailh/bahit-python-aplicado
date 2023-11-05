from argparse import ArgumentParser

argp = ArgumentParser(description="Example of description",epilog="Copyright 2023")

argp.add_argument('foo') # positional argument
argp.add_argument('--foo') # option foo
argp.add_argument('-f') # option f

# Just a positional argument
argp.add_argument('directory')

# List of option flags
argp.add_argument('-f', '--foo')