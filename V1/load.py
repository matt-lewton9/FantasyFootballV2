import csv
from icecream import ic
import pandas as pd

#load weekly daya
def load_weekly(wk, yr):

    weekly = str('data-master/data-master/weekly/'+str(yr)+"/week"+str(wk)+'.csv')

    with open(weekly, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #make database
        players = []
        for row in reader:          
            player = {}
            for header in row.keys():
                player[header] = row[header]
            players.append(player)

    return players

#load yearly data
def load_yearly(yr_strt, pos):
    ###TO_DO## must update usage to generate list based on start year argument
    
    yearlys = {}
    for y in range(yr_strt, 2020):
        yearlys[y] = str('data-master/data-master/yearly/'+str(y)+'.csv')

    #INIT databases and variables
    players = {}
    #load projections for consistancy
    projections = yearly_projections(pos)
    for player in projections.keys():
        players[player] = {}

    plyr_lst = []
    for year in yearlys.keys():
        with open(yearlys[year], newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            #make database
            for row in reader:
                #sort out players with projections
                if row['Player'] not in projections.keys():
                    continue

                #sort out wrong position
                if row['Pos'] != pos:
                    continue

                #add stats
                for header in row.keys():
                    if header not in ['Player', 'Tm', 'Pos']:
                        players[row['Player']][header+str(year)] = float(row[header])
                    else:
                        players[row['Player']][header] = row[header]
                    plyr_lst.append(row['Player'])

    players_final = {}
    for p in plyr_lst:
        players_final[p] = players[p]
    
    return players_final

#load yearly projections 2020 ONLY!!!!
def yearly_projections(pos):
    yearly = str('data-master/data-master/fantasypros/fp_projections.csv')

    with open(yearly, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #make database
        players = {}
        for row in reader:
            if row['Pos'] == pos:
                players[row['Player']] = {'pos' : row['Pos'], 'points' : float(row['FantasyPoints'])}

    return players

#load yearly actual points
def yearly_results(year, pos):
    yearly = str('data-master/data-master/yearly/'+str(year)+'.csv')
    with open(yearly, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #make database
        players = {}
        for row in reader:
            if row['Pos'] != pos:
                continue
            if row['FantasyPoints'] == '':
                players[row['Player']] = 0
            else:    
                players[row['Player']] = float(row['FantasyPoints'])

    return players