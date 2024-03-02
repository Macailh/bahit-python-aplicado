from json import dumps
from os import environ

method = environ["REQUEST_METHOD"]

status = "200 Ok"
json = dumps(dict(list=[1, 2, 3, 4]))

if method != "GET":
    status = "405 Method Not Allowed"
    json = "{}"

print("Content-type : application/json")
print(f"Status: {status}")
print("")
print(json)


from subprocess import Popen, PIPE

command = ["curl", "-i", "http://example.com/file.py"]
p = Popen(command, stdout=PIPE)
output = p.stdout.read()

print("Content-type : text/html; charset=utf-8")
print("")
print(output)
