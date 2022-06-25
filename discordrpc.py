from pypresence import Presence
import time
import psutil

start = int(time.time())
client_id = "990311942986010694" #application's client id; you only need to modify this to add images to rich presence
RPC = Presence(client_id)
RPC.connect()

while True: #keep repeating updating rich presence
    if ("xournalpp.exe" in (i.name() for i in psutil.process_iter())): #if Xournal++ is running
        RPC.update(
            large_image = "favicon-1", #name of your asset in discord's developer portal
            large_text = "Xournal++",
            details = "Editing a file",
            state = "Writing",
            start = start,
            buttons = [{"label": "Hello", "url": "https://google.com"}, {"label": "Discord", "url": "https://discord.gg/"}] #up to 2 buttons allowed
        )
        time.sleep(15) #can be as low as 15, depends on how often you want to update rich presence
    
    elif ("Acrobat.exe" in (i.name() for i in psutil.process_iter())): #if Adobe Acrobat is running
        RPC.update(
            large_image = "acrobat-reader", #name of your asset
            large_text = "Adobe Acrobat DC",
            details = "Reading a PDF",
            state = "Reading",
            start = start,
        )
        time.sleep(15)
    else:
        RPC.clear() #clear rich presence if no program is running
        time.sleep(15)