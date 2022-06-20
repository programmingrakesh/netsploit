import os
import subprocess
import time
from colorama import Fore, Back, Style
from threading import *


os.system("clear")
print(Fore.RED + r"""
  _   _     U _____ u   _____     ____       ____       _         U  ___ u                 _____
 | \ |"|    \| ___"|/  |_ " _|   / __"| u  U|  _"\ u   |"|         \/"_ \/      ___       |_ " _|
<|  \| |>    |  _|"      | |    <\___ \/   \| |_) |/ U | | u       | | | |     |_"_|        | |
U| |\  |u    | |___     /| |\    u___) |    |  __/    \| |/__  .-,_| |_| |      | |        /| |\
 |_| \_|     |_____|   u |_|U    |____/>>   |_|        |_____|  \_)-\___/     U/| |\u     u |_|U
 ||   \\,-.  <<   >>   _// \\_    )(  (__)  ||>>_      //  \\        \\    .-,_|___|_,-.  _// \\
 (_")  (_/  (__) (__) (__) (__)  (__)      (__)__)    (_")("_)      (__)    \_)-' '-(_/  (__) (__)

""")



if os.geteuid() != 0:
    exit("Run the script as root user. \nPlease try again.........")
else:
    exit = True


path = "netsploit/root"
while exit:
    cmd = input(Fore.BLUE + Back.BLACK + f"{path} > " + Style.RESET_ALL + " " + Fore.WHITE)
    if cmd == "exit":
        exit = False
        print(Fore.RED + "Goodbye!! \n")
    elif cmd == "help":
        if path == "netsploit/root":
            print(Fore.GREEN + "****************    HELP PAGE    ****************\n")
            print(Fore.WHITE + "help    -     Shows the Help page.")
            print(Fore.WHITE + "show   -     List the available modules.")
            print(Fore.WHITE + "select  -     select the modules.")
            print(Fore.WHITE + "clear   -     Clear the screen.")
            print(Fore.WHITE + "exit    -     To exit the program.\n")
        elif path == "netsploit/wifi":
            print(Fore.MAGENTA + "\nmodules    -    List the available modules.")
            print(Fore.MAGENTA + "cards    -    List the available wireless wifi cards.\n")
        elif path == "netsploit/bluetooth":
            print(Fore.CYAN + "\nmodules    -    List the available modules.")
            print(Fore.CYAN + "cards    -    List the available wireless wifi cards.\n")
    elif "select" in cmd:
        cmd = cmd.split(" ")
        if cmd[1] == "wifi":
             path = "netsploit/wifi"
        elif cmd[1] == "bluetooth":
             path = "netsploit/bluetooth"
        elif cmd[1] == "":
            print(Fore.RED + "Error : Please Enter The module name properly.\n")
    elif cmd == "back":
        path = "netsploit/root"
    
    elif cmd == "show":
        if path == "netsploit/root":
            print(Fore.GREEN + "\nwifi")
            print(Fore.GREEN + "bluetooth\n")
    elif cmd == "clear":
        os.system("clear")
    
    elif cmd == "modules":
        if path == "netsploit/wifi":
            print(Fore.LIGHTYELLOW_EX + "\nscan    -    Scan for the available list of AP's and Station's.")
            print(Fore.LIGHTYELLOW_EX + "deauth  -    Deauthenticate the clients form the AP.")
            print(Fore.LIGHTYELLOW_EX + "monitor <up/down> <interface>    -    To set the wireless card into monitor mode.\n")
        elif path == "netsploit/bluetooth":
            print(Fore.LIGHTCYAN_EX + "\nscan    -    Scan for the available list of bluetooth devices.")
            print(Fore.LIGHTCYAN_EX + "deauth  -    Deauthenticate the bluetooth devices.\n")    
        else:
            print(Fore.RED + "Please select the module.")

    elif cmd == "cards":
        if path == "netsploit/wifi":
            card = subprocess.getoutput("iwconfig")
            print(f"\n{card}\n")
        elif path == "netsploit/bluetooth":
            card = subprocess.getoutput("hciconfig")
            print(f"\n{card}\n")
        else:
            print(Fore.RED + "Please select the module.")
    
    elif "wifi.monitor" in cmd and path == "netsploit/wifi":
        cmd = cmd.split(" ")
        if cmd[1] == "up":
            os.system(f"airmon-ng start {cmd[2]}")
        elif cmd[1] == "down":
            os.system(f"airmon-ng stop {cmd[2]}")
        else:
            print(Fore.RED + "Error: Please enter the arguments correctly.")
    
    elif "wifi.scan" in cmd:
        if path == "netsploit/wifi":
            interface = cmd.split(" ")
            interface = interface[1]
            if "mon" in interface:
                def scan():
                    os.system(f"airodump-ng {interface}")
                    print(Fore.CYAN + "Press Ctl+C to stop the scan.")
                thread1 = Thread(target=scan())
                thread1.start()
            else:
                print(Fore.RED + "Please enter the arguments correctly.")
            
            
    elif "bluetooth.scan" in cmd:
        if path == "netsploit/bluetooth":
            def scan():
                print(Fore.RED + "Press Ctl+C to stop the scan.")
                os.system(f"hcitool scan")
            thread2 = Thread(target=scan())
            thread2.start()

    elif "bluetooth.deauth" in cmd:
        if path == "netsploit/bluetooth":
            print(Fore.RED + "Coming soon...\n")


    else:
        pass
