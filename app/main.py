import socket  # noqa: F401

server_socket = socket.create_server(("localhost", 4221))

connection, address = server_socket.accept() # wait for client
print(f"accepted connecton from {address}")

#read data
data = connection.recv(1024)

#send same data back 
connection.sendall(data)


