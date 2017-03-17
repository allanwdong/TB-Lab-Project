# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:48:46 2017

@author: allan
"""

import os
import json
import pickle
from collections import Counter


test_csv_105 = '/home/allan/Tuberculosis/Test105CSV'
test_csv_10 = '/home/allan/Tuberculosis/Test10CSV'
master_csv_dir = '/home/allan/Tuberculosis/CSVs'
hash_dir = '/home/allan/Tuberculosis/Hash'

def generator(suitcase):
    for macguffin in suitcase:
        yield macguffin
               
cnt = Counter()

csvdir = master_csv_dir
os.chdir(hash_dir)

# Creates list from Hash1 file
Hash1 = pickle.load(open('/home/allan/Tuberculosis/Hash/Hash1', 'r'))


# Creates dict from Hash2 and Hash3 files, contains 'u' (unicode string 
#  prefix) in dict

Hash2 = json.load(open('/home/allan/Tuberculosis/Hash/Hash2', 'r'))
Hash3 = json.load(open('/home/allan/Tuberculosis/Hash/Hash3'))

# Function creates dict of unique word pairs for all gene Data category string
#  'data_category' in list of genes 'genelst'


def Unique_Pairs_Overall(genelst, data_category):   
    pairs_list = []    
    for gene in Hash1:
        datastr_ = str(Hash3['{foo}_{bar}'.format(foo = gene,
                                                 bar = data_category)])
        datastrlower_ = datastr_.lower()
        datastrnopunc_ = datastrlower_.translate(None, '{}[]()=,.<>')
        indv_list = datastrnopunc_.split(' ')
        i = 0        
        while i  <= len(indv_list) - 2:
            x = indv_list[i] + ' ' + indv_list[i + 1]
            pairs_list.append(x)
            i += 1  
    for pair in generator(pairs_list):
        cnt[pair] += 1
    return cnt
    
grail1 = Unique_Pairs_Overall(csvdir,'Function')
with open('Unique_Pairs', 'w+') as fp1:
    json.dump(grail1, fp1, sort_keys = True, indent = 4)

