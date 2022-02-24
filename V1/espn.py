import requests
import json
from icecream import ic
from helpers import *

###### LOAD API #####
league_id = 1990824
year = 2018
week = 5
url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/' + \
      str(year) + '/segments/0/leagues/' + str(league_id) + \
      '?view=mMatchup&view=mMatchupScore'

r = requests.get(url,
                 params={'matchupPeriodId': week},
                 cookies={'swid': '{EA21070E-02EF-4DEF-A107-0E02EFFDEF99}',
                 		  'espn_s2': 'AECX0mM%2ByA9oQxG3nJFNs8Pwj2RF6ZaPK80tQxeN96PegbDNdneWPkICK5XcLPoGyGYA%2F6HR5uo2iAwmvE%2BPvOgCuBb4y8cV5blVOp53%2FnWZD4pFfuOMK0q0dlr%2B%2Fsn081K9T9tz5znW%2Bn%2BYoyc2Sgmdy9meREUKr2wiSO%2Bp1x%2FDAwLmybBZfhLkfs%2BBhWch9XOl4o4opD4NN66BX5apZrfpnQx1eDNKsr0%2FK6ZhE1%2FUHbwoL4TSCKww55%2FV04ZFVx49CPc7%2BdO8IgeDAW%2FHOP%2FE0gbSN%2B0nIextaSZHFzw2hA%3D%3D'})
d = r.json()

#####CODES#####
POSITION_CODES = {
        1 : 'QB',
        2 : 'RB',
        3 : 'WR',
        4 : 'TE',
        16 : 'D/ST',
        5 : 'K'
    }



##### LOAD DATA INTO DICT #####
#print(d['teams'][0]['roster']['entries'][0]['playerPoolEntry']['player']['stats'][0].keys())

#ic(d['teams'][0]['roster'])
for tm in d['teams']:
    tmid = tm['id']
    for p in tm['roster']['entries']:
        name = p['playerPoolEntry']['player']['fullName']
        injured = p['playerPoolEntry']['player']['injured']
        pos = POSITION_CODES[p['playerPoolEntry']['player']['defaultPositionId']]

        #Sort out DST inj status
        inj_status = None
        if pos != 'D/ST':
            inj_status = p['playerPoolEntry']['player']['injuryStatus']

        scores = get_scores(p['playerPoolEntry']['player']['stats'], 2)
        actual = scores[0]
        proj = scores[1]
        #print    
        #ic(name, pos, injured, inj_status, proj, actual)

ic(d['teams'][0]['roster']['entries'])
