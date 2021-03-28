import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print(f'Got connection from {addr}')
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()

# import socket
#
# # create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # get local machine name
# host = socket.gethostname()
#
# port = 9999
#
# # connection to hostname on the port.
# s.connect((host, port))
#
# # Receive no more than 1024 bytes
# tm = s.recv(1024)
#
# s.close()
#
# print("The time got from the server is %s" % tm.decode('ascii'))