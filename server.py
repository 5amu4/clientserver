import socket
'#using default (ipv4,TCP)'

server = socket.socket()
print("Server socket created")
'#binding'

server.bind(('localhost', 9999))
'#server connects to 3 clients at a given time'

server.listen(3)
print("Server waiting for connections")

while True:
    client, ipaddress = server.accept()
    name = client.recv(1024).decode()
    '#recieving data from client'
    print("Server is now connected with ", ipaddress, name)
    client.send(bytes("You're now connected with the server", 'utf-8'))
    '#recieving the data is to client'
    client.close()
    '#class to connection'
