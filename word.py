from pypresence import Presence
import time
import psutil
import os

start = int(time.time())
client_id = "990378068755488850"
RPC = Presence(client_id)
RPC.connect()

while ("WINWORD.EXE" in (i.name() for i in psutil.process_iter())):
    RPC.update(
        large_image = "word",
        large_text = "Microsoft Word",
        details = "Microsoft Word",
        state = "Editing a document",
        start = start,
    )
    time.sleep(15)

RPC.clear()
os.system("python appmanager.py")