# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:07:44 2017

@author: allan
"""

from bs4 import BeautifulSoup
import os
# import os

kdpE = '/home/allan/Tuberculosis/Test/kdpE'
pknG = '/home/allan/Tuberculosis/Test/pknG'
rv2031c = '/home/allan/Tuberculosis/Test/rv2031c'
 
pages = [kdpE, pknG, rv2031c]
#pages = [kdpE]


#def page_checker(html, namelist):
'''
namelist = namelist list
typelist = list of types from html
'''



def writer(namelist, templist):
    for i in templist:
        namelist.append(i)

def scanwrite(namelist, templist):
    for name in templist:    
        if name not in namelist:
            templist.append(name)
    writer(namelist, templist)
            
def htmlsoup_generater(html):
    htmlopen= open(html,'r')
    htmlfile = htmlopen.read()
    htmlsoup = BeautifulSoup(htmlfile, 'html.parser')
    htmlopen.close()
    yield htmlsoup


namelist = []
templist = []

def pages(directory):
    for page in directory:
        yield page

for gene in pages:
    htmlsoup = htmlsoup_generater(gene)
    table = htmlsoup.find_all('table')
    for i in range(1, 5):
        tableb = table[i].find_all('b')
        for label in tableb:
            templist.append(str(label.get_text()))
    scanwrite(namelist, templist)
    templist = []
print namelist
    
            
            

    

