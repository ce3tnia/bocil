import socket
import sys
import time
import os
import struct

print ("\nWelcome to the FTP server.\n\nTo get started, connect a client.")

# Initialise socket stuff
TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 2013 # Just a random choice
BUFFER_SIZE = 1024 # Standard size
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

print ("\nConnected to by address: {}".format(addr))

def upld():
    # Send message once server is ready to recieve file details
    conn.send("1".encode())
    # Recieve file name length, then file name
    file_name_size = struct.unpack("h", conn.recv(2))[0]
    print(file_name_size)
    file_name = conn.recv(file_name_size)
    file_name = file_name.decode()
    print("nama file "+file_name)
    # Send message to let client know server is ready for document content
    conn.send("1".encode())
    # Recieve file size
    file_size = struct.unpack("i", conn.recv(4))[0]

    # Initialise and enter loop to recive file content
    start_time = time.time()
    # print('nama file '+file_name)
    output_file = open(file_name, "wb")
    # This keeps track of how many bytes we have recieved, so we know when to stop the loop
    bytes_recieved = 0
    print ("\nRecieving...")
    while bytes_recieved < file_size:
        l = conn.recv(BUFFER_SIZE)
        output_file.write(l)
        bytes_recieved += BUFFER_SIZE
    output_file.close()
    print ("\nRecieved file: {}".format(file_name))
    # Send upload performance details
    conn.send(struct.pack("f", time.time() - start_time))
    conn.send(struct.pack("i", file_size))
    return

def list_files():
    print ("Listing files...")
    # Get list of files in directory
    listing = os.listdir(os.getcwd())
    # Send over the number of files, so the client knows what to expect (and avoid some errors)
    conn.send(struct.pack("i", len(listing)))
    total_directory_size = 0
    # Send over the file names and sizes whilst totaling the directory size
    for i in listing:
        # File name size
        conn.send(struct.pack("i", sys.getsizeof(i)))
        # File name
        conn.send(i.encode())
        # File content size
        conn.send(struct.pack("i", os.path.getsize(i)))
        total_directory_size += os.path.getsize(i)
        # Make sure that the client and server are syncronised
        conn.recv(BUFFER_SIZE)
    # Sum of file sizes in directory
    conn.send(struct.pack("i", total_directory_size))
    #Final check
    conn.recv(BUFFER_SIZE)
    print ("Successfully sent file listing")
    return

def dwld():
    conn.send("1".encode())est...
Connection unsuc
    file_name_length = structest...
Connection unsuc.unpack("h", conn.recv(2))[0]
    print (file_name_length)est...
Connection unsuc
    file_name = conn.recv(filest...
Connection unsuce_name_length)()
    print (file_name)est...
Connection unsuc
    if os.path.isfile(file_naest...
Connection unsucme):
        # Then the file existest...
Connection unsucs, and send file size
        conn.send(struct.pack("i", os.path.getsize(file_name)))
    else:
        # Then the file doesnest...
Connection unsucest...
Connection unsucest...
Connection unsuc't exist, and send error code
        print ("File name notest... valid")
        conn.send(struct.packConnection unsucest...("i", -1))
        returnConnection unsuc
    # Wait for ok to send file
    conn.recv(BUFFER_SIZE)
    # Enter loop to send fileest...
Connection unsuc
    start_time = time.time()
    print ("Sending file...")
    content = open(file_name, "rb")
    # Again, break into chunks defined by BUFFER_SIZE
    l = content.read(BUFFER_SIZE)
    while l:
        conn.send(l)
        l = content.read(BUFFER_SIZE)
    content.close()
    # Get client go-ahead, then send download details
    conn.recv(BUFFER_SIZE)
    conn.send(struct.pack("f", time.time() - start_time))
    return


def delf():
    # Send go-ahead
    conn.send("1".encode())
    # Get file details
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_length).decode()
    # Check file exists
    if os.path.isfile(file_name):
        conn.send(struct.pack("i", 1))
    else:
        # Then the file doesn't exist
        conn.send(struct.pack("i", -1))
    # Wait for deletion conformation
    confirm_delete = conn.recv(BUFFER_SIZE)
    if confirm_delete == "Y":
        try:
            # Delete file
            os.remove(file_name)
            conn.send(struct.pack("i", 1))
        except:
            # Unable to delete file
            print ("Failed to delete {}".format(file_name))
            conn.send(struct.pack("i", -1))
    else:
        # User abandoned deletionest...
Connection unsuc
        # The server probably recieved "N", but else used as a safety catest...
Connection unsucest...
Connection unsucch-allest...est...
Connection unsuc
Connection unsucest...
Connection unsuc
        print ("Delete abandoned by client!")est...est...est...est...est...
Connection unsuc
Connection unsucest...
Connection unsuc
Connection unsucest...est...
Connection unsuc
Connection unsucest...
Connection unsuc
Connection unsucest...est...
Connection unsuc
Connection unsucest...
Connection unsuc
Connection unsucest...est...est...
Connection unsuc
Connection unsuc
Connection unsucest...
Connection unsucest...
Connection unsuc
        returnest...est...est...
Connection unsuc
Connection unsucest...
Connection unsuc
Connection unsucest...est...
Connection unsuc
Connection unsucest...
Connection unsuc
est...est...est...
Connection unsuc
Connection unsucest...
Connection unsuc
Connection unsucest...est...
Connection unsuc
Connection unsuc
est...est...
Connection unsuc
Connection unsucest...
Connection unsuc
def quit():est...est...
Connection unsuc
Connection unsuc
    # Send quit conformationest...
Connection unsuc
    conn.send("1".encode())est...
Connection unsuc
    # Close and restart the serverest...
Connection unsuc
    conn.close()est...
Connection unsuc
    s.close()
    os.execl(sys.executable, sys.executable, *sys.argv)est...
Connection unsuc
est...
Connection unsuc
while True:est...
Connection unsuc
    # Enter into a while loop to recieve commands from clientest...
Connection unsuc
    print ("\n\nWaiting for instruction")est...
Connection unsuc
    data2 = conn.recv(BUFFER_SIZE)est...
Connection unsuc
    data = data2.decode();est...
Connection unsuc
    print ("\nRecieved instruction: {}".format(data))est...
Connection unsuc
    # Check the command and respond correctlyest...
Connection unsuc
    if data == "UPLD":est...
Connection unsuc
        upld()
    elif data == "LIST":
        list_files()
    elif data == "DWLD":
        dwld()
    elif data == "DELF":
        delf()
    elif data == "QUIT":
        quit()
    # Reset the data to loop
    data = None
