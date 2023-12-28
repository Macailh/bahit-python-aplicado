from os import system

info_command = "uname -a"
print("System information:")
system(info_command)

curl_command = "curl https://www.google.com/"
print("\nRequest to google:")
system(curl_command)

list_command = "ls -l"
print("\nList files:")
system(list_command)

