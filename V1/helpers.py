from icecream import ic

def get_scores(stats, wk):
    scores = [None, None]

    #ic(stats)

    for stat in stats:
        if stat['scoringPeriodId'] == wk:
            
            #actual
            if stat['statSourceId'] == 0:
                scores[0] = stat['appliedTotal']
            
            #projected
            elif stat['statSourceId'] == 1:
                scores[1] = stat['appliedTotal']
            
    return scores

