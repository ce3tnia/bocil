import time, socket, sys
print('Setup server...')
time.sleep(1)
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostname()
port = 1234
soc.bind((host_name, port))
print(host_name,'({})'.format(ip))
name = input('Enter name: ')
soc.listen(10)
print("waiting connection....")
connection, addr = soc.accept()
print("received coonection from...", addr[0], "(", addr[1],")\n")
print('connection established. scoonect from: {}, ({})'.format(addr[0], addr[1]))
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + 'has connected')
print('press [bye] to leave chat')
connection.send(name.encode())
while True:
    message = input('Me > ')
    if message == '[bye]':
        message = 'good night'
        connection.send(message.encode())
        print("\n")
        break
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client_name, '>', message)
