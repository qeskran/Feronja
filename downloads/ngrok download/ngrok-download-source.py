import os
import requests
import zipfile
#By Achilles
ngrok_url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip"
#By Achilles
ngrok_dir = "ngrok"
#By Achilles
if not os.path.exists(ngrok_dir):
    os.mkdir(ngrok_dir)
#By Achilles
ngrok_zip_path = os.path.join(ngrok_dir, "ngrok.zip")
response = requests.get(ngrok_url)
with open(ngrok_zip_path, "wb") as f:
    f.write(response.content)
#By Achilles
with zipfile.ZipFile(ngrok_zip_path, 'r') as zip_ref:
    zip_ref.extractall(ngrok_dir)
#By Achilles
os.remove(ngrok_zip_path)
#By Achilles
os.system(f'"{os.path.join(ngrok_dir, "ngrok.exe")}" tcp 9999')
#By Achilles