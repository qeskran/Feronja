import os
import sys
import platform
import winreg
import subprocess
import fade
def replace_server_details(file_path, server_address, server_port):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
#By Achilles
    for i in range(len(lines)):
        if 'server_address = (' in lines[i]:
            lines[i] = f'server_address = (\'{server_address}\', {server_port})\n'
    with open(file_path, 'w') as file:
        file.writelines(lines)
#By Achilles
#By Achilles
server_port = input("\033[38;5;208mEnter the server port for server.py: \033[0m")
replace_server_details('server-backup.py', '0.0.0.0', server_port)