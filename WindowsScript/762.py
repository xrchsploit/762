# Modules

import os
import subprocess
import time

# Colors for text
class bcolors:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    FLASH = '\033[5m'

print(bcolors.FLASH + bcolors.RED + bcolors.BLUE + """
_________  ________________  
\______  \/  _____/\_____  \ 
    /    /   __  \  /  ____/ 
   /    /\  |__\  \/       \ 
  /____/  \_____  /\_______ \
               


""" + bcolors.NORMAL)

print("Make sure you ran this as administrator, if you didn't close this and re-run it as admin!")

time.sleep(5)


# Starts System Security Auditing 

forensics_q = input("Have you done your forensics? y/n: ")

if forensics_q == str("n"):
	print("Go do those real quick then come back.")
	quit()
elif forensics_q == str("y"):
	print("Proceeding...")

print("\n"+ bcolors.BLUE + "Go start updates installation while the rest of the script works." + bcolors.NORMAL)

print(bcolors.GREEN + 
"""
Go through firefox settings and ensure its default browser

Go to privacy and security and enable strict mode

Delete cookies and site data when firefox is closed

Ask to save passowrds and logins

Disable autofill addresses and credit cards

Block deceptive content

Block Dangerous Downloads

Warn about unwanted software

Enable HTTPS only mode

Script will stop for 15 seconds for you to do this.
""" + bcolors.NORMAL)

time(sleep 15)

print(bcolors.RED + 
"""Starting password complecity settings... 
Maximum Password Age -> 30
Minimum Password Age -> 10
Minimum Password Length -> 12
""" + bcolors.NORMAL)

os.system("net accounts /maxpwage:30")
os.system("net accounts /minpwage:10")
os.system("net accounts /minpwlen:12")


