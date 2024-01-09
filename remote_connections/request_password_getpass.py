from ftplib import FTP
from getpass import getpass
ftp = FTP()

host = "examplehost.com"
port = 21
ftp.connect(host, port)

# Get user and password
username = input("Ingrese su nombre de usuario: ")
password = getpass("Ingrese su contraseña: ")

# Login in FTP server
ftp.login(username, password)

# You can now execute FTP commands, such as listing directories, uploading or downloading files, etc.
# For example, to list files in the current directory:
ftp.retrlines('LIST')

# Close connection
ftp.quit()
