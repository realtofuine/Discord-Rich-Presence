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
client_id = "990831184512679946"
RPC = Presence(client_id)
RPC.connect()

while ("Zoom.exe" in (i.name() for i in psutil.process_iter())):
    get_idle_duration()
    if(get_idle_duration() > 300):
        RPC.update(
            large_image = "zoom",
            large_text = "Zoom Meetings",
            details = "Zoom Meetings",
            state = "Idle",
            start = start,
        )
    else:
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