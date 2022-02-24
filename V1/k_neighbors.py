from icecream import ic

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from load import yearly_projections, load_yearly, yearly_results

def FP_evidence_n_labels(pos, start_year):
    evidence  = []
    labels = []
    yearly_stats = load_yearly(start_year, pos)

    projections = yearly_projections(pos)
    actuals = yearly_results(2020, pos)

    #Iterates through all players in 2020 only
    #Unsage: use YEAR = 2019 to predict future, Year =  2020 to predict present   
    for player in yearly_stats.keys():
        if player not in actuals.keys() or player not in projections.keys():
            continue

        p_stats = []

        #cehcks for position or allows all position if pos is None
        if yearly_stats[player]['Pos'] == pos or pos == None:
            
            #gets actual and projected
            actual = actuals[player]
            #actual = yearly_stats[player]['FantasyPoints2019'] This code is wrong, it looks at 2019 points, not 2020, but i'll leave it in here as a comment
            proj = projections[player]['points']

            #assigns labels
            if proj != 0:
                if float(actual) >= float(proj):
                    label = True
                else:
                    label = False
            else: 
                continue

            labels.append(label)   

            #adds all evidence data except points and strings
            for header in yearly_stats[player].keys():
                if header not in ['Player', 'Tm', 'Pos'] :
                    p_stats.append(yearly_stats[player][header])

            evidence.append(p_stats)

    for e in evidence:
        ic(len(evidence))        
    return (evidence, labels)


    #Implement K neighbors
def k_neighbors(evidence, labels, k, tst_sze):
    #Load Data and split into test/train sets
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size= tst_sze
    )

    # Train model and make predictions
    model = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    predictions = model.predict(X_test) 

    #return percent correctly determined
    return evaluate(y_test, predictions)


#evaluate predicted T/F
def evaluate(labels, predictions):
   
    #init counting variables
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    
    #assign true positives and negatives
    for i in range(len(labels)):
        if labels[i] == 1:
            if predictions[i] == 1:
                TP +=1
            else:
                TN+=1
        else:
            if predictions[i] == 0:
                FN +=1
            else:
                FP +=1

    corr = round(100*(TP+FN)/len(predictions), 3)
    sen =  round(100*TP/(TP+FN), 3)
    spe = round(100*TN/(FP+TN), 3)

    return TP+FN, FP+TN, sen, spe, corr
 
    ####### INCOMPADIBLE WITH GLOBALS #######
"""
    #Get Evidence and Labels
def ESPN_evidence_n_labels(teams, pos):
    evidence = []
    labels = []
    
    #get all possible keys
    keys = []
    for tm in teams:
        roster  = tm.roster
        for p in roster:
            if p.position not in ['D/ST', 'K']:
                for key in p.stats[WEEK]['breakdown'].keys():
                    if key not in keys:
                        keys.append(key)

    #iterate over all rostered players
    for tm in teams:
        roster  = tm.roster
        for p in roster:
            #if p.position not in ['D/ST', 'K'] and p.injured == False:
            if p.position == pos and p.injured == False:

                breakdown = []
                #adds to evidence list
                for key in keys:
                    if key in p.stats[WEEK]['breakdown']:
                        breakdown.append(p.stats[WEEK]['breakdown'][key])
                    else:
                        breakdown.append(0)
                evidence.append(breakdown)

                #adds to labels list
                if p.stats[WEEK]['points'] >= p.stats[WEEK]['projected_points']:
                    labels.append(True)
                else:
                    labels.append(False)
                
    return (evidence, labels)

"""