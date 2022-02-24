from icecream import ic

import matplotlib.pyplot as plt
import pandas as pd

from k_neighbors import *

##### FP K NEAREST NEIGHBOR #####
#Unsage: use YEAR = 2019 or earlier to predict future, Year =  2020 to predict present
def k_test_sen_spe(pos, TRIALS, START_YEAR, TEST_SIZE, k_range):
    

    df = pd.DataFrame(None, columns = ['Trials', 'Data Season', 'Projection Season', 'Position', 'k Neighbors', 'avg correct', 'avg incorrect', 'avg sensitivity', 'avg specitivity', 'avg accuracy'])

    for k in range(1, k_range, 2):

        #Init results
        results = { 'avg correct' : 0, 
                    'avg incorrect': 0, 
                    'avg sensitivity': 0, 
                    'avg specitivity': 0, 
                    'avg accuracy': 0}
        results['Trials'] = TRIALS
        results['Data Season'] = START_YEAR
        results['Projection Season'] = 2020
        results['Position'] = str(pos)
        results['k Neighbors'] = k

        #Runk TRIALS trials
        for i in range(TRIALS):
            evidence, labels = FP_evidence_n_labels(pos, START_YEAR)
            cor, inc, sen, spe, acc = k_neighbors(evidence, labels, k, TEST_SIZE)
            results['avg correct'] += cor/TRIALS
            results['avg incorrect'] += inc/TRIALS
            results['avg sensitivity'] += sen/TRIALS
            results['avg specitivity'] += spe/TRIALS
            results['avg accuracy'] += acc/TRIALS
            #print('percent complete: '+ str(100*i/TRIALS)+ '%')

        #for key in results.keys():
        #    print(key, ': ', results[key]/TRIALS)

        #add to dataframe
        df = df.append(results, ignore_index = True)

    #write dataframe to csv
    #df.to_csv('k_neighbors.csv')


    k_N = df['k Neighbors']
    sens = df['avg sensitivity']
    spec = df['avg specitivity']
    accu = df['avg accuracy']

    diff = []
    for i in range(len(accu)):
        diff.append(abs(sens[i]-spec[i]))

    # plot Sensitivity, Specitivity and average
    # Label Nonetype pos as all
    if pos == None:
          pos = 'All'
    plt.plot(k_N, sens, label = "avg sensitivity", color = 'g')
    plt.plot(k_N, spec, label = "avg specitivity", color = 'r')
    plt.plot(k_N, accu, label = "avg accuracy", color = 'b')
    plt.plot(k_N, diff, label = 'difference', color = 'k')
    plt.ylabel('Percent')
    plt.xlabel('k Values')
    plt.title(str(START_YEAR)+'-2020 Performence for k Nearest Neighbors, pos: '+ pos + ', Trials: '+str(TRIALS))
    plt.legend()
    #plt.show()
    plt.savefig('sen-spec'+str(pos)+str(START_YEAR)+'.png')