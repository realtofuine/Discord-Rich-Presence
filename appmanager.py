from pypresence import Presence
import time
import psutil
import os

while True: #keep repeating updating rich presence
    if ("xournalpp.exe" in (i.name() for i in psutil.process_iter())): #if Xournal++ is running
        os.system("python xournal.py")
    elif ("Acrobat.exe" in (i.name() for i in psutil.process_iter())): #if Adobe Acrobat is running
        os.system("python adobeacrobat.py")
    elif ("WINWORD.EXE" in (i.name() for i in psutil.process_iter())): #if Word is running
        os.system("python word.py")
    else:
        time.sleep(15)
        