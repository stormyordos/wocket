#!/usr/bin/python3
import urllib.request
import requests
import argparse
import string
import json


print("\
  _/          _/                      _/                    _/      \n\
 _/          _/    _/_/      _/_/_/  _/  _/      _/_/    _/_/_/_/   \n\
_/    _/    _/  _/    _/  _/        _/_/      _/_/_/_/    _/        \n\
 _/  _/  _/    _/    _/  _/        _/  _/    _/          _/         \n\
  _/  _/        _/_/      _/_/_/  _/    _/    _/_/_/      _/_/      \n\
")

##TODO: add list of features (get files from channels, from groups, list messages)

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--room", required=True,
	help="full name of the chat room to parse")
ap.add_argument("-a", "--address", required=True,
	help="domain name part of the Rocket Chat URL")
ap.add_argument("-t", "--token", required=True,
	help="personal Auth Token for the Rocket Chat API")
ap.add_argument("-i", "--id", required=True,
	help="personal User ID for the Rocket Chat API")
ap.add_argument("-f", "--folder", required=False,
	help="output folder for the downloads (default: current folder)")
ap.add_argument("-m","--messages", required=False,
	help="switch, also list all messages from the chat (default: attached files)",action='store_true')
ap.add_argument("-x","--nofiles", required=False,
	help="switch, do not download attached files",action='store_true')
ap.add_argument("-c","--channel", required=False,
	help="switch, look for a channel (open room) instead of a group (closed room)",action='store_true')
args = vars(ap.parse_args())

#setting variables
counter = 0
dled = 0
msgCount = 0
roomType = "groups"
if args["channel"] == True:
    roomType = "channels"
if args["folder"] is None:
    folder = "."
else:
    folder = args["folder"].rstrip("/")

#querying the Rocket Chat room for files
if args["nofiles"] == False:
    url = 'https://'+args["address"]+'/api/v1/'+roomType+'.files?roomName='+args["room"]+'&count=0'
    reqFiles = urllib.request.Request(url,headers={"X-Auth-Token":args["token"],"X-User-Id":args["id"]})
    #parsing response
    r = urllib.request.urlopen(reqFiles).read()
    cont = json.loads(r.decode('utf-8'))

    #parsing JSON answer
    print("###################################################################")
    for item in cont['files']:
        counter += 1
        try:
            print("Name:", item['name'])
            print("RID:", item['rid'])
            print("TypeGroup:", item['typeGroup'])
            print("Path:", item['path'])
            print("URL:", item['url'])
            if args["address"] not in item['url']:
                url = 'https://' + args["address"] + item['url']
            else:
                url = item['url']
            r = requests.get(url, headers={"X-Auth-Token":args["token"],"X-User-Id":args["id"]})
            with open(folder+'/'+item['name'], 'wb') as f:
                f.write(r.content)
                f.flush
                f.close
            print("-------------------------------------------------------------------")
            dled += 1
        except Exception as e:
            print('   >>>> '+str(e))
            print()

#querying the Rocket Chat room for files
if args["messages"] == True:
    url = 'https://'+args["address"]+'/api/v1/'+roomType+'.messages?roomName='+args["room"]+'&count=0'
    reqMsg = urllib.request.Request(url,headers={"X-Auth-Token":args["token"],"X-User-Id":args["id"]})

    #parsing response
    r = urllib.request.urlopen(reqMsg).read()
    cont = json.loads(r.decode('utf-8'))

    #parsing JSON answer
    print("###################################################################")
    for item in cont['messages']:
        msgCount += 1
        try:
            print("User:", item['u']['username'])
            print("Timestamp:", item['ts'])
            print("Message:", item['msg'])
            print("-------------------------------------------------------------------")
        except Exception as e:
            print('   >>>> '+str(e))
            print()

##print formated
print("###################################################################")
if args["nofiles"] == False:
    print("Number of files found: ", counter)
    print("Number of files downloaded: ", dled)
if args["messages"] == True:
    print("Number of messages found: ", msgCount)
