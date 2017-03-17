# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 00:56:39 2017

@author: allan
"""



import os
import csv
import json
import pickle


test_csv_105 = '/home/allan/Tuberculosis/Test105CSV'
test_csv_10 = '/home/allan/Tuberculosis/Test10CSV'
master_csv_dir = '/home/allan/Tuberculosis/CSVs'

os.chdir('/home/allan/Tuberculosis/Hash')


def pages(directory):
    for page in directory:
        yield page

csvdir = master_csv_dir


field_names = ['Type', 'Data']

# Hash1 list of all genes by Rv Number
# Saved with pickle

hashlist = []
for i in pages(os.listdir(csvdir)):
    hashlist.append(i.strip('.csv'))
hashlist2 = sorted(hashlist) 

with open('Hash1', 'w+') as fb:
    pickle.dump(hashlist2, fb)

      

# Hash2 hashmap - Key = "GeneName" : 
#                 Value = (List of all 'Types' without null 'Data' value)
# Saved with json

Hash2 = {}
for i in pages(os.listdir(csvdir)):    
    csvfile_ = '%s/%s' % (csvdir, i)
    with open(str(csvfile_), 'r') as csvfile:  
        reader = csv.DictReader(csvfile, 
                                fieldnames = field_names
                                ) 
        templist = []
        for row in reader:
            if row['Data'] != 'null':
                templist.append(row['Type'])
        Hash2['{name}'.format(name = i.strip('.csv'))] = templist

with open('Hash2', 'w+') as fp:
    json.dump(Hash2, fp, sort_keys = True, indent = 4)
 
 
# Hash3 hashmap - Key = "'GeneName'_'Type'" :
#                 Value = "Data"   
# Saved with json         
Hash3 = {}
for i in pages(os.listdir(csvdir)):    
    csvfile_ = '%s/%s' % (csvdir, i)
    with open(str(csvfile_), 'r') as csvfile:  
        reader = csv.DictReader(csvfile, 
                                fieldnames = field_names
                                ) 
        templist = []
        for row in reader:
            Hash3['{name}_{key}'.format(name = i.strip('.csv'), 
                                        key = row['Type']
                                        )
                  ] = row['Data']

with open('Hash3', 'w+') as fp:
    json.dump(Hash3, fp, sort_keys = True, indent = 4)

                  

'''
field_names = ['Type', 'Data']
metB = '/home/allan/Tuberculosis/Test10CSV/metB.csv'
csvfile = open(metB)
reader = csv.DictReader(csvfile, fieldnames = field_names)
'''