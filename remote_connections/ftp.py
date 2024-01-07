from ftplib import FTP

ftp = FTP()

ftp.connect("example.com", 21)
ftp.set_pasv(True)
ftp.login("username", "password")
ftp.quit()

# Other methods
# list directories dir()  dir("route/")
# create directory mkd("route/")
# Move directory cwd("route/")
# Delete directory rmd("route/")
# Get actual directory pwd()
# Recover remote file retrbinary("RETR origen", open("/", "w").write)
# Send local file storbinary("STOR /remote.txt", open("/origin/local.txt", "r"))
# Delete file delete("file/to/delete")
# Rename file rename("origin", "destination")