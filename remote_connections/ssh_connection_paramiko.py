from paramiko import SSHClient, AutoAddPolicy

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.load_system_host_keys()
ssh.connect("123.45.67.89", 22, "user", "password")

input, output, error = ssh.exec_command("ls -la")

input.write("Input waiting for the command \n")
output.read()
ssh.close()