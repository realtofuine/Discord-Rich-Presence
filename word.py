from pypresence import Presence
import time
import psutil
import os
from ctypes import Structure, windll, c_uint, sizeof, byref

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

start = int(time.time())
client_id = "990378068755488850"
RPC = Presence(client_id)
RPC.connect()

while ("WINWORD.EXE" in (i.name() for i in psutil.process_iter())):
    get_idle_duration()
    if(get_idle_duration() > 60):
        RPC.update(
            large_image = "word",
            large_text = "Microsoft Word",
            details = "Microsoft Word",
            state = "Idle",
            start = start,
        )
    else:
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