from pypresence import Presence
import time
import psutil
import os

start = int(time.time())
client_id = "990356931321413712" #application's client id; you only need to modify this to add images to rich presence
RPC = Presence(client_id)
RPC.connect()

while ("Acrobat.exe" in (i.name() for i in psutil.process_iter())): #keep repeating updating rich presence
    RPC.update(
        large_image = "acrobat-reader", #name of your asset in discord's developer portal
        large_text = "Adobe Acrobat DC",
        details = "Adobe Acrobat DC",
        state = "Reading a PDF",
        start = start,
    )
    time.sleep(15) #can be as low as 15, depends on how often you want to update rich presence

RPC.clear()
os.system("python appmanager.py") #restart appmanager.py if Adobe Acrobat is not running