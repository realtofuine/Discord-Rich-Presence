from pypresence import Presence
import time
import psutil
import os

start = int(time.time())
client_id = "990311942986010694" #xournal's client id
RPC = Presence(client_id)
RPC.connect()

while ("xournalpp.exe" in (i.name() for i in psutil.process_iter())): #keep repeating updating rich presence
    RPC.update(
        large_image = "favicon-1", #name of your asset in discord's developer portal
        large_text = "Xournal++",
        details = "Editing a file",
        state = "Writing",
        start = start,
        #if you want meaningful buttons, uncomment the below line
        # buttons = [{"label": "Hello", "url": "https://google.com"}, {"label": "Discord", "url": "https://discord.gg/"}] #up to 2 buttons allowed
    )
    time.sleep(15) #can be as low as 15, depends on how often you want to update rich presence

RPC.clear()
os.system("python appmanager.py") #restart appmanager.py if Xournal++ is not running