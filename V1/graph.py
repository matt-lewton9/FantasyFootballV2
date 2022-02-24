import matplotlib.pyplot as plt

#accuracy of espn projections for season or week
def ESPN_proj_accuracy(teams, wk, pos):
    proj = []
    actual = []

    for tm in teams:
        roster  = tm.roster
        for p in roster:

            #if p.position not in ['D/ST', 'K'] and p.injured == False:
            if p.position == pos or pos == None:

                #adds points to lists
                if p.stats[wk]['projected_points'] != 0 and p.stats[wk]['points'] != 0:
                    proj.append(p.stats[wk]['projected_points'])
                    actual.append(p.stats[wk]['points'])

    return {'proj': proj, 'actual': actual}


#graph
def graph_cmp_hist(data, parA, parB, pos, b, wk, yr):
    if pos == None:
        pos = 'All'
    if wk == 0:
        wk = 'Reg Season'
    else:
        wk = str(wk)
    plt.hist(data[parA], b, alpha=0.5, color = 'b', label=parA)
    plt.hist(data[parB], b, alpha=0.5, color='g', label=parB)
    plt.legend(loc='upper right')
    plt.ylabel('Fequency')
    plt.xlabel('Points')
    plt.title(parA+' vs '+ parB + ': '+pos+', week '+ str(wk) + " " + str(yr))

    plt.show()


#graph percent error between 2 datasets
def graph_pct_error(proj, actual, pos, b, xlim, wk, yr):

    #calculate gross % error
    err = []
    for i in range(len(proj)):
        err.append(100*abs(actual[i]-proj[i])/proj[i])

    #create position and week title
    if pos == None:
        pos = 'All'
    if wk == 0:
        wk = 'Reg Season'
    else:
        wk = str(wk)

    #create graph and labels
    plt.ylabel('Frequency')
    plt.xlabel('% Error')
    if xlim != None:
        plt.xlim(0, xlim)
    plt.hist(err, b, color = 'r')
    plt.title(pos+': % error, week: ' + str(wk) + " " + str(yr))

    plt.show()


