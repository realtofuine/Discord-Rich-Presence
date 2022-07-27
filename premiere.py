import os
import time

import psutil
from pypresence import Presence

start = int(time.time())
client_id = "1001669236231520316" #application's client id; you only need to modify this to add images to rich presence
RPC = Presence(client_id)
RPC.connect()

while ("Adobe Premiere Pro.exe" in (i.name() for i in psutil.process_iter())): #keep repeating updating rich presence
    RPC.update(
        large_image = "premiere", #name of your asset in discord's developer portal
        large_text = "Adobe Premiere Pro",
        details = "Adobe Premiere Pro",
        state = "Editing a video",
        start = start,
    )
    time.sleep(15) #can be as low as 15, depends on how often you want to update rich presence

RPC.clear()
os.system("python appmanager.py") #restart appmanager.py if Adobe Acrobat is not running
