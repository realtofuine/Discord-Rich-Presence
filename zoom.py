from pypresence import Presence
import time
import psutil
import os

start = int(time.time())
client_id = "990831184512679946"
RPC = Presence(client_id)
RPC.connect()

while ("Zoom.exe" in (i.name() for i in psutil.process_iter())):
    RPC.update(
        large_image = "zoom",
        large_text = "Zoom Meetings",
        details = "Zoom Meetings",
        state = "In a Zoom Meeting",
        start = start,
    )
    time.sleep(15)

RPC.clear()
os.system("python appmanager.py")