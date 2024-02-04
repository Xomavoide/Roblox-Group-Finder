import os
import threading
import requests
import random
from dhooks import Webhook
import time

time.sleep(5)

webhook_url = 'https://discordapp.com/api/webhooks/1203460768591388672/dy8fDuicMI2kgCPyo-kBzB0-IyJ-mtkl_m5R8RNsL0cGLRgwtrSNxkGuyKZpOpyBMJ1h'
hook = Webhook(webhook_url)

def groupfinder():
    id = random.randint(0, 5007736)
    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}")

    print(f"Checking group: {id}")

    if 'owned' not in r.text:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        if 'isLocked' not in re.text:
            # Check if 'publicEntryAllowed' key is True in the response JSON
            if 'publicEntryAllowed' in re.json() and re.json()['publicEntryAllowed'] == True:
                hook.send(f'Found group: https://www.roblox.com/groups/group.aspx?gid={id}')
                print(f"[+] Found group: {id}")
            else:
                print(f"[-] Group is Closed or No Public Entry Allowed: {id}")
        else:
            print(f"[-] Group is Locked: {id}")
    else:
        print(f"[-] Group Already Owned: {id}")

threads = int(input("[-] How many threads: "))

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()
