# Discord-Rich-Presence
Custom Discord Rich Presence based on running apps using a Python script

## Preinstalled apps

- Adobe Acrobat DC
- Adobe Premiere Pro
- Xournal++
- Microsoft Word
- Zoom

## Setting your apps
In `appmanager.py`, copy the elif statements and add the .exe files of the apps you want the script to detect. Use `xournal.py` as a template to create another file that includes the rich presence details of the app you want to detect. Modify the stuff under `RPC.update` to set the images and details you want the rich presence to include for that app.

The images can only be modified by creating your own clients in the [Discord Developer Portal](https://discord.com/developers/applications) for each app you want a rich presence for and then copying the number under `APPLICATION ID` into each file corresponding to the detected app.

You can run the script automatically at startup using a batch file and Windows Task Scheduler.

## Usage

Run `appmanager.py` to start the script.

You can automate this at startup by creating a task in Windows Task Scheduler that runs `rundiscordrp.bat` at startup.

## Thinking about
I am trying to make the script more efficient. Currently, every 15 seconds, the script runs again and consumes CPU.