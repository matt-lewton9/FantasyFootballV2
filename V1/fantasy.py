from icecream import ic
from espn_api.football import League

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#from load import *
from graph import *
from k_neighbors import *
from analysis import *

##### Constants #####
TEST_SIZE = 0.4
WEEK = 0
START_YEAR = 2018
TRIALS = 1

def main():

    k_range = 3
    pos = 'QB'

    k_test_sen_spe(pos, TRIALS, START_YEAR, TEST_SIZE, k_range)


    ###### LOAD LEAGUE #####
    #league = League(league_id=1990824, year=YEAR, espn_s2='AECX0mM%2ByA9oQxG3nJFNs8Pwj2RF6ZaPK80tQxeN96PegbDNdneWPkICK5XcLPoGyGYA%2F6HR5uo2iAwmvE%2BPvOgCuBb4y8cV5blVOp53%2FnWZD4pFfuOMK0q0dlr%2B%2Fsn081K9T9tz5znW%2Bn%2BYoyc2Sgmdy9meREUKr2wiSO%2Bp1x%2FDAwLmybBZfhLkfs%2BBhWch9XOl4o4opD4NN66BX5apZrfpnQx1eDNKsr0%2FK6ZhE1%2FUHbwoL4TSCKww55%2FV04ZFVx49CPc7%2BdO8IgeDAW%2FHOP%2FE0gbSN%2B0nIextaSZHFzw2hA%3D%3D', swid='{EA21070E-02EF-4DEF-A107-0E02EFFDEF99}')


    ###### DIFFERENT ANALYZERS ######
    """
    ### ESPN K Neighbors Machine Learning###
    evidence, labels = ESPN_evidence_n_labels(teams, 'WR')
    k_neighbors(evidence, labels, 2)
    """

    
    #### Graph comparative datasets###
    """
    POS = None

    ESPN = ESPN_proj_accuracy(league.teams, WEEK, POS)
    graph_cmp_hist(ESPN, 'proj', 'actual', POS, 15, WEEK, YEAR)
    graph_pct_error(ESPN['proj'], ESPN['actual'], POS, 100, 200, WEEK, YEAR)
    """

    ##### LOAD BIG DATA #####

    """
    # Season Data
    season = []
    for w in range(1, 17):
        season.append(load_weekly(w, YEAR))
    """

main()