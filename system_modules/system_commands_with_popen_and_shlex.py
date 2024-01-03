from shlex import split
from subprocess import Popen

command = "ls -la /home/macailh/dev/courses/bahit-python-aplicado/system_modules"
process = Popen(split(command))