from http.client import HTTPConnection

# GET example
http = HTTPConnection("google.com", port=80, timeout=10)
http.request("GET", "/foo/bar")
get_response = http.getresponse()
print("GET Response: ", get_response.read().decode())

#POST example
params = "name=Jane&lastname=Doe"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

http.request("POST", "/foo/bar", headers=headers, body=params)
post_response = http.getresponse()
print("POST Response: ", post_response.read().decode())

http.close()