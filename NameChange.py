# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:41:14 2016

@author: allan
"""

import os

Tuberculosis = '/home/allan/Tuberculosis'


badprefix = "quicksearch.php?gene+name="
badsuffix = "&submit=Search"

for filename in os.listdir(Tuberculosis):
    if filename.startswith(badprefix):
        os.rename(filename, filename.replace(badprefix, '', 1))
    if filename.endswith(badsuffix):
        os.rename(filename, filename.replace(badsuffix, '', 1))
        
        
        