import socket
import time
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)
while True:
    clientsocket.addr = serversocket.accept()
    print("Got a connection form %s" %(addr))
    currentTime = time.ctime(time.time())+"\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
