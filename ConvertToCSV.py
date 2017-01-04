# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 23:55:57 2016

@author: allan
"""



import re
from bs4 import BeautifulSoup
import csv


# html API
# Note: 'Tuberculosis' is easy to mispell 
gene = '/home/allan/Tuberculosis/kdpE'
htmlfile= open(gene,'r').read()
htmlsoup = BeautifulSoup(htmlfile, 'html.parser')


# Find title
h3str = str(htmlsoup.find_all("h3"))
h3match = re.match('.*?\:\ (.*)\<', h3str)

# Note: type(gene_name) = 'str'
gene_name = h3match.group(1)

'''
List of Types following code doesn't work for:
Mutation, Coordinates;CDS, Protein Sequence in FASTA format (Mildly different +
concact lines), Gene Ontology (separate phrases), M. bovis/marinum/smegmatis
(make sure these are same for all pages), 

Focus on Function, Product, and Comments for query later

'''
'''

Type_List = ('Gene name', 'Rv number', 'Type', 'Function', 'Product', 
             'Comments', 'Molecular mass (Da)', 'Isoelectric point', 
             'Gene length (bp)', 'Protein length', 'Location (kb)',
             'Functional category', 'Proteomics' , 'Transcriptome', 'Regulon',
             'Protein Data Bank','PFAM', 'CDC1551', 'UniProt', 'TDR Targets', 
             'TBDB')
'''
# Iteration over html tables to create 'Type Title' list
# tablei = table[i]
# table1 = Gene Name - Location (Kb)
# table2 = Functional category
# table3 = Mutation - Regulon
# table4 = Coordinates
# table5 = Protein FASTA
# table6 = "Structural information"
# table7 = "Orthologs/Cross-references"
# table8 = "Interacting Drugs/Compounds"
# table9 = "Expression Data"

# Expanded code for how table iterator works, appends what should be Type 
# labels to typelist[]
'''
table = htmlsoup.find_all('table')
table1 = table[1]
table1_ = table1.find_all('b')

foo = []
for i in table1_:
    foo.append(str(i.get_text()))
'''
typelist = []

table = htmlsoup.find_all('table')

for i in range(1, 10):
    table_ = table[i].find_all('b')
    for label in table_:
        typelist.append(str(label.get_text()))

'''
# Note: This doesn't work - figure out how to get it to work later
open('%s.csv', 'rb') % (gene_name)
'''    


# Need to define how to scan for type:data in html
# Replace commas with /t 




# Data_scribe
# Supposed to scan validity of most Type::Data pairings 
# Does not work for Coordinates: Start/Stop
# Does not add url links

'''
def Data_scribe(NavHtml):
    try:
        NavHtml.parent
        NavHtml.parent.parent
        NavHtml.parent.parent.next_sibling
    except:
        writer.writerow({'type' : '{foo}'.format(foo = Type_val) , 
                         'data' : '{bar}'.format(bar = 'null')})
    
    Data = str(NavHtml.parent.parent.next_sibling.get_text())
            Data_val = Data.replace(',', '\t')       
            writer.writerow({'type' : '{foo}'.format(foo = Type_val) , 
                             'data' : '{bar}'.format(bar = Data_val)})
    
    
    NavHtml.parent.parent == type(None):
        writer.writerow({'type' : '{foo}'.format(foo = Type_val) , 
                         'data' : '{bar}'.format(bar = 'null')})        
   
    except:   
        if type(NavHtml.parent.parent.next_sibling) == type(None):
            writer.writerow({'type' : '{foo}'.format(foo = Type_val) , 
                             'data' : '{bar}'.format(bar = 'null')})
        else:
            Data = str(NavHtml.parent.parent.next_sibling.get_text())
            Data_val = Data.replace(',', '\t')       
            writer.writerow({'type' : '{foo}'.format(foo = Type_val) , 
                             'data' : '{bar}'.format(bar = Data_val)})
 '''                        
typelist_mod = typelist

                         
with open('{name}.csv'.format(name = gene_name), 'w') as csvfile:
    fieldnames = ['type', 'data']    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='null')
 
#    writer.writerow({'type' :  , 'data' : }) 
    #% ('test1', 'test2')
 

    for i in typelist:
        Type_val = '%s' % i
        NavHtml = htmlsoup.find(string=Type_val)
                
        
        try:        
            NavHtml.parent
            NavHtml.parent.parent
            NavHtml.parent.parent.next_sibling
        except:
            typelist_mod = typelist_mod.remove(i)
            writer.writerow({'type' : '{foo}'.format(foo = Type_val) , 
                             'data' : '{bar}'.format(bar = 'null')})
        
    for i in typelist_mod:
        Type_val = '%s' % i 
        NavHtml = htmlsoup.find(string=Type_val)
#       Data_scribe(NavHtml)   
        Data = str(NavHtml.parent.parent.next_sibling.get_text())
        Data_val = Data.replace(',', '\t')       
        
        writer.writerow({'type' : '{foo}'.format(foo = Type_val) , 
                           'data' : '{bar}'.format(bar = Data_val)})      

                     
# CSV DictWriter Test   
#    writer.writerow({'type' : 'test1' , 'data' : 'test2'})    
     
    
    
    
    
    
    