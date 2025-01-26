import socket
import time

SERVER_HOST= "0.0.0.0"
SERVER_PORT=8080
server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#adding optional settings to change the behaviour of the socket 
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1) # SO stands for socket and REUSEADDR-> reuse address. 

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Listening on port {SERVER_PORT}...")

while True:
        client_socket, client_address= server_socket.accept()
        request= client_socket.recv(1024).decode() #(bufsize: int, flags: int = ..., /) -> bytes
        print (request)