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

time.sleep(15)

print(bcolors.RED + 
"""Starting password complexity settings... 
Maximum Password Age -> 30
Minimum Password Age -> 10
Minimum Password Length -> 12
Lockout Duration -> 30
Lockout Threshold -> 5
Lockout Window -> 10


""" + bcolors.NORMAL)

os.system("net accounts /maxpwage:30")
os.system("net accounts /minpwage:10")
os.system("net accounts /minpwlen:12")
os.system("net accounts /lockoutduration:30")
os.system("net accounts /lockoutthreshold:5")
os.system("net accounts /lockoutwindow:10")

# Notepad function
os.system("cls")

print(bcolors.BLUE + 
"""A Notepad will open, set the options and be sure to not delete something on accident.

PasswordComplexity = 1
LockoutBadCount = 5
ResetLockoutCount = 10
RequireLogonToChangePassword = 1
EnableGuestAccount = 0

AuditSystemEvents = 1
AuditLogonEvents = 1
AuditObjectAccess = 1
AuditPrivilegeUse = 1
AuditPolicyChange = 1
AuditAccountManage = 1
AuditProcessTracking = 1
AuditAccountLogon = 1


!!! DO NOT FORGET TO SAVE THE CHANGES !!!
""" + bcolors.NORMAL)

time.sleep(3)

os.system("secedit.exe /export /cfg C:\secconfig.cfg")
os.system("start notepad C:\secconfig.cfg")
os.system("secedit.exe /configure /db %windir%\securitynew.sdb /cfg C:\secconfig.cfg /areas SECURITYPOLICY")

os.system("cls")

print("""
Now you have to manually audit using secpol.msc

It will open up, go to the Local Policies >> Security Options and make sure everything looks good.
""")

time.sleep(3)
os.system("cls")

print("""
Ok now you have to analyze the firewall settings in secpol.msc

It should open, go to Windows Defender Firewall with Advanced Security >> The firewall
Now on the right hand side click firewall properties

1. Turn on the firewall
2. Reject incoming
3. Allow outgoing

Now check the Connection Security Rules and make sure theres no sus rules in place
Then check Inbound Rules and Outboud Rules 
""")


time.sleep(5)
os.system("cls")
print("This concludes the Secpol.msc audits...")

# Done with Account Auditing

print("Moving on to editing gpedit.msc *Its much easier to audit using gui*")
time.sleep(3)
os.system("cls")
print("""
When the editor opens go to User configuration >> Administrative Templates >> All Settings
(If this isnt an option good luck)

Go through and disable things that need to be disabled
""")

time.sleep(3)

os.system("gpedit.msc")

