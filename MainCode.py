#ClothingCollector

#RequiredImports
from asyncio import sleep
import urllib
from urllib.request import urlopen
import json
import time

#CreateFileToStoreInformation
StoredIDs = open("StoredOneLineInformation.txt", "w")
GroupID = 0 #PlaceGroupIDHere!

#CollectAllClothingURL
RequestURL = "https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={}&CreatorType=2&Limit=30".format(GroupID)

#RobloxJSONKey
JSONKey = ""

print("Clothing ID Collector, Activated")

while JSONKey != ("None"):
        URLResponse = urlopen(RequestURL)
        JSONResponse = json.loads(URLResponse.read())

        JSONKey = JSONResponse["nextPageCursor"]
        JSONData = JSONResponse["data"]

        for x in JSONData:
            ClothingName = x["name"]
            ClothingID = x["id"]

            ConvertedName = str(ClothingName)
            ConvertedID = str(ClothingID)
            
            print(ClothingName)
            print(ClothingID)

            StoredIDs.write(ConvertedName+" : "+ConvertedID+"\n")

        RequestURL = "https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId=2897916&CreatorType=2&Limit=30&Cursor=" + JSONKey
        print("New Key:", JSONKey)
        time.sleep(1)

print("Clothing ID Collector, Deactivated")
        
