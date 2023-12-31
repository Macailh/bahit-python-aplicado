from shlex import split
from subprocess import Popen, PIPE

command = "ls -la ."
process = Popen(split(command), stdout=PIPE, stderr=PIPE)
output = process.stdout.read()
errors = process.stderr.read()

if not errors:
    print("No errors")
    print(output)
else:
    print("Errors")
    print(errors)