import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
s.connect((host, port))
tm = s.recv(1024)
s.close()
print("the time got from server is %s" % tm.encode('ascii'))
