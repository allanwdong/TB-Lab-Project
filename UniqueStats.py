# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:44:26 2017

@author: allan
"""

import os
import json
import pandas as pd
import numpy as np
import decimal
# import seaborn as sbn


master_csv_dir = '/home/allan/Tuberculosis/CSVs'
hash_dir = '/home/allan/Tuberculosis/Hash'
Unique_Single = '/home/allan/Tuberculosis/Hash/Unique_Single'
Unique_Pairs = '/home/allan/Tuberculosis/Hash/Unique_Pairs'



csvdir = master_csv_dir
os.chdir(hash_dir)



# Creates dict from Unique Single and Unique Pairs files, contains 'u'   
#  (unicode string prefix) in dict

UniqueSingle = json.load(open(Unique_Single, 'r'))
UniquePairs = json.load(open(Unique_Pairs, 'r'))

keysSingle = []
for key in UniqueSingle:
    keysSingle.append(key)

keysPairs = []
for key in UniquePairs:
    keysPairs.append(key)

dfUniqueSingle = pd.DataFrame(UniqueSingle.items(), index = keysSingle,
                              columns = ['Word', 'Word Count'])
                    
dfUniquePairs = pd.DataFrame(UniquePairs.items(), index = keysPairs,
                             columns = ['Pair', 'Pair Count'])

# Test area
test_pair = '/home/allan/Tuberculosis/Hash/Testpair'
testpair= json.load(open(test_pair, 'r'))

keysTest = []
for key in testpair:
    keysTest.append(key)


dftest = pd.DataFrame(testpair.items(), index = keysTest, 
                      columns= ['Pair', 'Pair Count'])

TotSingleCnt = int(dfUniqueSingle['Word Count'].sum())
TotPairsCnt = int(dfUniquePairs['Pair Count'].sum())



def NaiveBayes(row):
    decimal.Context(prec = 12)
    tempwordlst = str(row['Pair']).split(' ')
    word1 = tempwordlst[0]
    word2 = tempwordlst[1]
    count1 = dfUniqueSingle.loc['{word}'.format(word = word1), 'Word Count']
    count2 = dfUniqueSingle.loc['{word}'.format(word = word2), 'Word Count']
    countpair = dfUniquePairs.loc['{word_pair}'.format(word_pair = row['Pair']),
                                  'Pair Count']
    WordFrac1 = float(count1)/TotSingleCnt
    WordFrac2 = float(count2)/TotSingleCnt
    PairFrac = float(countpair)/TotPairsCnt
    return (WordFrac1 * WordFrac2) / PairFrac


# dftest['Bayes'] = dftest.groupby(NaiveBayes, axis = 0 )




dftest['Naive Bayes'] = dftest.apply(NaiveBayes, axis = 1)
    
        









