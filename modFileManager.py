import json


# Function opens the data file and adds a new entry to the dictionary
def addServer(server, homeID):
    # Load serverDict from json
    with open("data.txt", 'r') as file_object:
        serverDict = json.load(file_object)
    
    # Checks that server doesnt already exist
    if not server in serverDict.keys():
        serverDict[server] = {
            "server": server,
            "homePanel": homeID,
            "blacklist":[],
            "strikes":{
            },
            "CUPS":{
                
            }
        }
    
    # Converts the dictionary back into json, assigns it to json_object
    json_object = json.dumps(serverDict, indent=4)
    # Writes the json to the data file
    with open("data.txt", 'w') as file_object:
        file_object.write(json_object)


# Retrieves Dictionary entry for the passed in server
def getServerData(server):
    with open("data.txt", 'r') as file_object:
        serverList = json.load(file_object)
    #print(serverList)
    return serverList[str(server)]

# Stores the data passed in to the data file
def storeServerData(server_object):
    with open("data.txt", 'r') as file_object:
        serverList = json.load(file_object)
    serverList[str(server_object["server"])] = server_object
    json_object = json.dumps(serverList, indent=4)
    with open("data.txt", 'w') as file_object:
        file_object.write(json_object)

# Test entry
data = {
    "server": 354676547567,
    "blacklist": ["word10", "word11"],
    "strikes": {
        "minttin#1111": 1,
    }
}
