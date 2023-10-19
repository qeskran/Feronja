import os
import subprocess
import requests
#By Achilles
python_installer_url = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe"
#By Achilles
installer_path = "python_installer.exe"
#By Achilles
response = requests.get(python_installer_url)
with open(installer_path, "wb") as f:
    f.write(response.content)
#By Achilles
subprocess.run([installer_path])
#By Achilles
os.remove(installer_path)
#By Achilles
print("Python has been installed.")
