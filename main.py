import subprocess
import platform
import sys
import os
import time
from pystyle import *
from colorama import *


os.system("cls")
os.system("title xenox pinger by norze")
banner = """
▀████    ▐████▀    ▄████████ ███▄▄▄▄    ▄██████▄  ▀████    ▐████▀ 
  ███▌   ████▀    ███    ███ ███▀▀▀██▄ ███    ███   ███▌   ████▀  
   ███  ▐███      ███    █▀  ███   ███ ███    ███    ███  ▐███    
   ▀███▄███▀     ▄███▄▄▄     ███   ███ ███    ███    ▀███▄███▀    
   ████▀██▄     ▀▀███▀▀▀     ███   ███ ███    ███    ████▀██▄     
  ▐███  ▀███      ███    █▄  ███   ███ ███    ███   ▐███  ▀███    
 ▄███     ███▄    ███    ███ ███   ███ ███    ███  ▄███     ███▄  
████       ███▄   ██████████  ▀█   █▀   ▀██████▀  ████       ███▄ 


"""
text = """EASY PINGER BY NORZE#0001"""

banner = Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(banner))
text = Colorate.Diagonal(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(text))

print(banner)
print(text)

ip = input(f"\n\n\n{Fore.WHITE}[{Fore.LIGHTBLUE_EX}?{Fore.WHITE}] {Fore.LIGHTBLUE_EX}Please Enter Your Ip Address {Fore.WHITE}-> ")
numbers = int(input(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}?{Fore.WHITE}] {Fore.LIGHTBLUE_EX}Please Enter The Number Of Ping {Fore.WHITE}-> "))

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0


def main():
    for _ in range(numbers):
        time.sleep(1)
        host = sys.argv[1] if len(sys.argv) == 2 else f'{ip}'
        result = ping(host)
        if result:
            print(f'{host} est accessible')
        else:
            print(f'{host} est inaccessible')
       
        input(Fore.CYAN+"\n[!] Operation finish ")


if __name__ == '__main__':
    main()
