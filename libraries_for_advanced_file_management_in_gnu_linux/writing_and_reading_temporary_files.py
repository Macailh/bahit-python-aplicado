from tempfile import TemporaryFile, gettempdir

with TemporaryFile() as tmp:
    # File exist
    tmp.write(b"Byte string")
    tmp.seek(0) # Move xursor to byte 0
    content = tmp.read()

with TemporaryFile() as tmp:
    tmp.write(b"Example")
    tmp_dir = gettempdir()
    print(tmp_dir)

# File doesnt exist
