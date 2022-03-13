import socket, sys

port = 443
host = "689292b.com"
filename = "//"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall((filename + "\r\n").encode())

while (1):
    buf = s.recv(1)
    if not buf:
        break
    sys.stdout.write(buf)