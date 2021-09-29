'''''
Samuel
Client Server interaction
09/28/2021
'''
import socket

client = socket.socket()

client.connect(('localhost', 9999))

name = input('localhost')

client.send(bytes(name, 'utf-8'))

print(client.recv(1024).decode())
