# Discord-Rich-Presence
Custom Discord Rich Presence based on running apps using a Python script

## Setting your apps
In `discordrpc.py`, add the .exe files of the apps you want the script to detect. Modify the stuff under `RPC.update` to set the images and details you want the rich presence to include.

The images can only be modified by creating your own client in the [Discord Developer Portal](https://discord.com/developers/applications) and then copying the number under `APPLICATION ID`.

You can run the script automatically at startup using a batch file and Windows Task Scheduler.

## Thinking about
I am not skilled in python at all, so I am still trying to think of a way to change the name of the client for every app (so it doesn't just say Playing DiscordRPC) as the status.