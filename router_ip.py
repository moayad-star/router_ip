# Modules
from os import system as UI
try:
    import requests
except (ModuleNotFoundError,FileNotFoundError):
    UI("pip install requests ; clear")
    import requests

# Check your connection status
try:
    test_connect = requests.get("http://www.google.com")
except (requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout): # Handling errors
    exit("\033[;41;mYou are offline !\033[;40;m")

# start
try:
    for num_one_point in range(256):
            for num_sec_point in range(256):
                link = f"http://192.168.{str(num_one_point)}.{str(num_sec_point)}"
                try:
                    url = str(requests.get(link,timeout=0.04))
                except (requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout): # Handling errors
                    continue
                if url == "<Response [200]>":
                    print(f"\033[;37;m[+] Success \033[;32;m  {link}")
except KeyboardInterrupt:
    exit("\nExit...")
