# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:44:26 2017

@author: allan
"""

import os
import json
import pandas as pd
import numpy as np


master_csv_dir = '/home/allan/Tuberculosis/CSVs'
hash_dir = '/home/allan/Tuberculosis/Hash'
testhash = '/home/allan/Tuberculosis/Hash/Test'


csvdir = master_csv_dir
os.chdir(hash_dir)


test = open(testhash, 'r')
# Creates dict from Hash2 and Hash3 files, contains 'u' (unicode string 
#  prefix) in dict

Hash2 = json.load(open('/home/allan/Tuberculosis/Hash/Hash2', 'r'))
Hash3 = json.load(open('/home/allan/Tuberculosis/Hash/Hash3', 'r'))


Test = json.load(test)

'''
def UniqueNaiveBayes(Hash2address, Hash3address):
    Hash2 = json.load(open(Hash2address, 'r'))
    Hash3 = json.load(open(Hash3address, 'r'))
    for pair in Hash3:
        


keys = []

for key in Test:
    keys.append(key)
    
'''

df = pd.DataFrame(Test.items(), columns= ['Pair', 'Pair Count'])



