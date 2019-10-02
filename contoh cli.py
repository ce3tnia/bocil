import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print ("UDP target IP:", UDP_IP)
print("UDP target Port", UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((UDP_IP, UDP_PORT))
while 1:
    pesan = input('pesan anda : ')
    sock.send(pesan.encode())
