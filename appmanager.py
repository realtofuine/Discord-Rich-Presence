import os
import time

import psutil
from pypresence import Presence

while True: #keep repeating updating rich presence
    if ("xournalpp.exe" in (i.name() for i in psutil.process_iter())): #if Xournal++ is running
        os.system("python xournal.py")
    elif ("Acrobat.exe" in (i.name() for i in psutil.process_iter())): #if Adobe Acrobat is running
        os.system("python adobeacrobat.py")
    elif ("WINWORD.EXE" in (i.name() for i in psutil.process_iter())): #if Word is running
        os.system("python word.py")
    elif ("Zoom.exe" in (i.name() for i in psutil.process_iter())): #if Zoom is running
        os.system("python zoom.py")
    elif ("Adobe Premiere Pro.exe" in (i.name() for i in psutil.process_iter())): #if Adobe Premiere Pro is running
        os.system("python premiere.py")
    else:
        time.sleep(15)
        