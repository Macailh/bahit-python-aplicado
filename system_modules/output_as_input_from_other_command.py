from shlex import split
from subprocess import Popen, PIPE

ls_command = "ls -la ."
grep_command = "grep '10:51'"

ls_process = Popen(split(ls_command), stdout=PIPE, stderr=PIPE)
print(ls_process.stdout.read())

grep_process = Popen(split(grep_command), stdin=ls_process.stdout, stdout=PIPE, stderr=PIPE)
print(grep_process.stdout.read())