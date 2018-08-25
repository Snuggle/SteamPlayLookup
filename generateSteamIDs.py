#!/usr/bin/env python3
import json
import requests

API_SteamURL = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
InputPath = 'Games.txt'
OutputPath = 'AppIDs.txt'


class SteamPlayLookup:
    def __init__(self, API_SteamURL, PathList): # This is the main thingy. directly in the constructor
        print("Welcome to SteamPlayLookup!\n\nFetching Steam API AppList...")
        SteamAPIList = self.grabJSON(API_SteamURL)

        print("Reading your input list...")
        InputList = open(PathList[0]).readlines()

        print("Looking up Game IDs!")
        OutputList = self.lookup(InputList, SteamAPIList['applist']['apps'])

        print("Now outputting to your file...")
        OutputFile = open(PathList[1], 'w')
        for ID in OutputList:
            OutputFile.write(f"{ID}\n")

        print(f"Finished.")

    def lookup(self, lookup_list, api_json):
        OutputList = []
        for game in lookup_list:
            currentAppID = "NULL" # If cannot be found in API, return "NULL"
            for app in api_json:
                if app['name'].lower().strip() == game.lower().strip(): # Clean whitespace, case-insensitive
                    currentAppID = app['appid']
                    break
            print(f"{currentAppID} - {game}")
            OutputList.append(currentAppID)

        return OutputList

    def grabJSON(self, url):
        response = requests.get(url=url)
        data = response.json()
        return data

SteamPlayLookup(API_SteamURL, [InputPath, OutputPath])
