import os
import time
import sys
import requests
import math
print("""                             ____            __ 
   _________  ___  ___  ____/ / /____  _____/ /_
  / ___/ __ \/ _ \/ _ \/ __  / __/ _ \/ ___/ __/
 (__  ) /_/ /  __/  __/ /_/ / /_/  __(__  ) /_  
/____/ .___/\___/\___/\__,_/\__/\___/____/\__/  
    /_/                                         
    """)
print("List of servers: GDrive, Discord, OneDrive, Dropbox")
server = input("Input: ")
link = ""
match server.lower():
    case "gdrive":
        link = "https://drive.google.com/uc?export=download&id=1diuCQBRK-TKAwmb4XDRScMScsYI-c3bC"
    case "discord":
        link = "https://cdn.discordapp.com/attachments/874765339945222155/887018466828242975/download"
    case "onedrive":
        link = "https://onedrive.live.com/download?cid=08CA482FDF566B6F&resid=8CA482FDF566B6F%21106&authkey=AM4wjBZqneFUirg"
    case "dropbox":
        link = "https://www.dropbox.com/s/hziks07oagrtzf6/download?dl=1"
    case _:
        print("Please re-run the program unless you put a invalid server on purpose.")
        exit()
start = time.time()
print("Downloading...")
r = requests.get(link, allow_redirects=True,stream=1)
end = time.time()
megabytes =  len(r.content)/1038150
seconds = end-start
speed = megabytes/seconds
roundedmbs = round(megabytes,2)
roundedseconds = round(seconds,2)
roundedspeed = round(speed,2)
print("Downloaded " + str(roundedmbs) + " MB in " + str(roundedseconds) + "s")
print(" ")
print("Average Speed: " + str(roundedspeed) + "MB/s")