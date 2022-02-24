import csv
from icecream import ic
import json

"""
PROGRAM DESCRIPTION:
Convert yearly csv files of fantasy football data into json files for all players containing that player's yearly stats.
The json files will be easier to feed into K nearest neighbors later.
"""

# Get common categories from spreadsheets from start year to end year
def getCategories(startYear, endYear):
    Categories = []

    for year in range(startYear, endYear): #iterate through all years to 2020
        datasheet = f"data/yearly/{year}.csv" #make datasheet string
       
        with open(datasheet, newline='') as csvfile: #open datasheet and make reader
            reader = csv.DictReader(csvfile)
            
            if year == startYear: #for first year, init all fieldnames
                Categories = reader.fieldnames
            else:
                catTemp = [] #init temp holder for overlapping categories
                for cat in reader.fieldnames:
                    if cat in Categories: #if cat is in categories list, add to temo
                        catTemp.append(cat)
                Categories = catTemp #make overlapping list new category template
    
    return Categories #return list of common categories to main


def getPlayerDict(Categories, startYear, endYear): #get a player master dictionary using only common categories
    Players = {} #init emtpy player dict
    
    for year in range(startYear, endYear): #iterate through all years to 2020
            datasheet = f"data/yearly/{year}.csv" #make datasheet string
        
            with open(datasheet, newline='') as csvfile: #open datasheet and make reader
                reader = csv.DictReader(csvfile)

                for row in reader: #iterate over all players in spreadsheet
                    playerStats = {} #init temp dict of current players stats
                    for stat in Categories: #iterate through all stats
                        playerStats[stat] = row[stat]
                        
                    if playerStats["Player"] not in Players.keys(): #make new empty dict for a new player
                        Players[playerStats["Player"]] = {}
                        Players[playerStats["Player"]]["Pos"] = playerStats["Pos"]
                   
                    playerStats.pop("Player") #remove player name from every year entry
                    Players[row["Player"]][year] = playerStats #add player's stats to dict

    return Players #return player master dict


def jsonOut(Players): #Save all players as Json files, sorted by position
    for playerName in Players.keys(): #iterate through all players
        player = Players[playerName] #get player
        playerPos = player["Pos"] #get player position

        if playerPos not in ["QB", "RB", "WR","TE"]: #if position not sortable, add to NA folder
            playerPos = "NA"

        with open(f'Players/{playerPos}/{playerName}.json', 'w') as fp: #save player json to folder sorted by position
            json.dump(player, fp, indent=4)

def main(): # main
    startYear = 1970 #init start year for players
    endYear = 2021 #init end year for players

    Categories = getCategories(startYear, endYear) #get a list of common categories from start year to end year

    Players = getPlayerDict(Categories, startYear, endYear) #get a player master dictionary using only common categories

    jsonOut(Players) #Save all players as Json files, sorted by position

main()