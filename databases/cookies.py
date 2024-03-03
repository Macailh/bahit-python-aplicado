from http import cookies

# Create a SimpleCookie object
cookie = cookies.SimpleCookie()

# Add cookies
cookie["username"] = "john_doe"
cookie["language"] = "en"

# Set additional attributes for the cookie
cookie["username"]["path"] = "/"
cookie["language"]["path"] = "/"

# Set expiration date for the cookie
cookie["username"]["expires"] = 3600  # Expire in 1 hour

# Get the cookie header
cookie_header = cookie.output(header="")

# Print the cookie header
print(cookie_header)

# To set the cookie in an HTTP response, you would add the cookie_header to the response.
# For example:
# response.headers.add('Set-Cookie', cookie_header)
