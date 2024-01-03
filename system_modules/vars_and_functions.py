from shlex import split
from subprocess import Popen, PIPE

ls = "ls la ."
grep = "grep '10:51'"

ps_ls = Popen(split(ls), stdout=PIPE, stderr=PIPE)

if ps_ls.stderr.read():
    exit("Abrupt termination with errors in ls command")

ps_grep = Popen(split(grep), stdin=ps_ls.stdout, stdout=PIPE, stderr=PIPE)