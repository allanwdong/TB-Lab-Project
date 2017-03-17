# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:57:35 2017

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
Hash3 = json.load(open('/home/allan/Tuberculosis/Hash/Hash3', 'r'))


# Function creates dict of unique word count in Data category "Function"
#  for imput 'gene', stripped of characters: '{}[]()=,.<>'

def Unique_Words_Function(gene):
    datastr = str(Hash3['{foo}_Function'.format(foo = gene)])    
    datastrlower = datastr.lower()
    datastrclean = datastrlower.translate(None, '{}[]()=,.<>')
    datals = datastrclean.split(' ')
    for word in generator(datals):
        cnt[word] += 1
    return cnt
    
    
'''
for i in generator(os.listdir(csvdir)):
    gene = i.strip('.csv')    
    print Unique_Words_Function(gene)    
'''

# Function creates dict of unique word count for all gene Data category string
#  'data_category'  in list of genes 'genelst'

def Unique_Words_Overall(genelst, data_category):    
    datastrcol = ''
    for gene in Hash1:
        datastr = str(Hash3['{foo}_{bar}'.format(foo = gene,
                                                 bar = data_category)])
        datastrlower = datastr.lower()
        datastrcol += ' ' + datastrlower
    datastrclean = datastrcol.translate(None, '{}[]()=,.<>')
    datals = datastrclean.split(' ')
    for word in generator(datals):
        cnt[word] += 1
    return cnt

foobar = Unique_Words_Overall(csvdir, 'Function')        
with open('Unique_Overall', 'w+') as fp:
    json.dump(foobar, fp, sort_keys = True, indent = 4)
  

