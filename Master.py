# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:34:44 2017

@author: allan
"""

import os.path
import ConvertCSV
import csv




test_105 = '/home/allan/Tuberculosis/Test105'
test_10 = '/home/allan/Tuberculosis/Test10'
master = '/home/allan/Tuberculosis/tuberculist.epfl.ch'
test10CSV = '/home/allan/Tuberculosis/Test10CSV'
test105CSV = '/home/allan/Tuberculosis/Test105CSV'
final = '/home/allan/Tuberculosis/CSVs'


# List of Type names to iterate over
namelist = ('Gene name', 'Rv number', 'Type', 'Function', 'Product', 
             'Comments', 'Molecular mass \(Da\)', 'Isoelectric point', 
             'Gene length \(bp\)', 'Protein length', 'Location \(kb\)',
             'Functional category', 'Proteomics' , 'Transcriptome', 'Regulon',
             'Protein Data Bank','PFAM', 'CDC1551', 'UniProt', 'TDR Targets', 
             'TBDB')

# Creates generator to iterate over pages in address 'directory', returns 
#  'page'
def pages(directory):
    for page in directory:
        yield page
# Creates generator to iterate over values in 'namelist', returns 'name'
def nameiter(namelist):
    for name in namelist:
        yield name


# save_dir = The directory CSVs are saved to
save_dir = final
os.chdir(save_dir)

# page_dir = directory with raw html page files
page_dir = master

# Iterates over html pages, writes csv file titled with gene name, creates 
#  csv.Dict of 'Type':'Data', with 'Data' == 'null' if corresponding 'Type'
#   doesn't exist in the html page


field_names = ['Type', 'Data']    
 
for gene in pages(os.listdir(page_dir)):
    html = '%s/%s' % (page_dir, gene)
    htmlfile = ConvertCSV.htmlfiler(html)
    checklist = ConvertCSV.namecheck(htmlfile, namelist)
    faillist = ConvertCSV.namefail(htmlfile, namelist)
    with open('{name}.csv'.format(name = gene), 'w+') as csvfile:    
        writer = csv.DictWriter(csvfile, 
                                fieldnames = field_names, 
                                restval = 'null'
                                )
        for name in nameiter(checklist):
            draft = ConvertCSV.filer(htmlfile, name)
            data = ConvertCSV.cleaner(draft)          
            writer.writerow({'Type' : '{foo}'.format(foo = name), 
                             'Data' : '{bar}'.format(bar = data)}
                             )
        for name in nameiter(faillist):    
            data = ConvertCSV.filer(htmlfile, name)
            writer.writerow({'Type' : '{foo}'.format(foo = name), 
                             'Data' : '{bar}'.format(bar = 'null')}
                             )




# Ignore following: for testing purposes only
'''
kdpE = '/home/allan/Tuberculosis/Test10/kdpE'
pknG = '/home/allan/Tuberculosis/Test10/pknG'
rv2031c = '/home/allan/Tuberculosis/Test10/rv2031c'
metB = '/home/allan/Tuberculosis/Test10/metB'
MTB000060 = '/home/allan/Tuberculosis/Test10/MTB000060'

checklist = []
passlist = []

htmlfile = ConvertCSV.htmlfiler(MTB000060)

def nameiter(namelist):
    for name in namelist:
        yield name

def namecheck(htmlfile, namelist):
    import regex 
    checklist = []    
    for name in namelist:
        if regex.search('<b>{foo}</b></TD><TD>(.*?)</TD>'.format(foo=name), 
                     htmlfile) != None:
            print 'Upper' + ': ' + name
        if regex.search('<b>{foo}</b></td><td>(.*?)</td>'.format(foo=name),
                     htmlfile) != None:
            print 'lower' + ': ' + name
           
    return checklist

print namecheck(htmlfile, namelist)



def filer(htmlfile, name):
    import regex
    i = 0    
    reg = ''
    regex1= '<b>{foo}</b></td><td>(.*?)</td>'
    regex2= '<b>{foo}</b></TD><TD>(.*?)</TD>'
    if regex.search(regex1.format(foo=name), htmlfile) != None:
        reg = regex1
        i = 1
    else:
        pass
    if regex.search(regex2.format(foo=name), htmlfile) != None:
        reg = regex2
        i = 2
    else:
        pass
    textsearch = regex.search(reg.format(foo=name), htmlfile)    
    try:    
        data = textsearch.group(1)
        return data
    except:
        return "does not work"
 
    try:    
        raw_text = textsearch.group(1)
        return raw_text
    except:
        return "Doesn't group"
    
    data = 'Error: Reference ConvertCSV.filer'
    if i == 1:
        halfdone = raw_text.lstrip('<b>{foo}</b></td>'.format(foo=name))
        data = halfdone.rstrip ('</td>')
    else:
        pass
    if i == 2:
        halfdone = raw_text.lstrip('<b>{foo}</b></TD>'.format(foo=name))
        data = halfdone.rstrip ('</TD>')
    else:
        pass
    print raw_text    
    print halfdone    
    print data

if True:
    html = metB
    gene = 'metB'
    htmlfile = ConvertCSV.htmlfiler(html)
    checklist = ConvertCSV.namecheck(htmlfile, namelist)
    faillist = ConvertCSV.namefail(htmlfile, namelist)
    with open('{name}.csv'.format(name = gene), 'w') as csvfile:    
        fieldnames = ['type', 'data']    
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='null')
        for name in nameiter(checklist):
            data = filer(htmlfile, name)
            writer.writerow({'type' : '{foo}'.format(foo = name) , 
                             'data' : '{bar}'.format(bar = data)})
        for name in nameiter(faillist):    
            data = filer(htmlfile, name)
            writer.writerow({'type' : '{foo}'.format(foo = name) , 
                             'data' : '{bar}'.format(bar = 'null')})
'''

