# Wocket
---
Simple tool leveraging Rocket Chat API to query messages and attached files from a room

```
usage: wocket.py [-h] -r ROOM -a ADDRESS -t TOKEN -i ID [-f FOLDER] [-m] [-x]

optional arguments:
  -h, --help            show this help message and exit
  -r ROOM, --room ROOM  full name of the chat room to parse
  -a ADDRESS, --address ADDRESS
                        domain name part of the Rocket Chat URL
  -t TOKEN, --token TOKEN
                        personal Auth Token for the Rocket Chat API
  -i ID, --id ID        personal User ID for the Rocket Chat API
  -f FOLDER, --folder FOLDER
                        output folder for the downloads (default: current folder)
  -m, --messages        also list all messages from the chat (default: attached files)
  -x, --nofiles         do not download attached files
```

# Features
* Downloads all attached files from a specific Rocket Chat room
* Lists all messages from a specific Rocket Chat room

# Installation
* ` git clone https://github.com/stormyordos/wocket.git `
* Requires urllib and json packages
* Tested on Python 3.x / Linux OpenSuSE. Should work on most other distributions supporting Python ... may even work with Windows

# Examples
* Requests all attached files from a room and downloads them in the current directory: `./wocket.py --room=myroom -a rocket.yolo.team --token=XXXX --id=XXXXX`
* Requests both messages and attached files from a room, and downloads files to a specific directory : `./wocket.py --room=myroom -a rocket.yolo.team --token=XXXX --id=XXXXX -m -f /home/yolo/Downloads`
* Requests only messages from a room : `./wocket.py --room=myroom -a rocket.yolo.team --token=XXXX --id=XXXXX -m -x`
