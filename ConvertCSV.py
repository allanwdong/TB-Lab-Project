# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:34:44 2017

@author: allan
"""




# Open file; create python readable instance of 'html' file
def htmlfiler(html):
    htmlopen = open(html, 'r')
    htmlfile = htmlopen.read()
    htmlopen.close()    
    return htmlfile


# Note: 'Coordinates', 'Start', 'End', and 'Orientation' need separate check
# Note: 'Protein Seq in FASTA' needs separate check


# Check values in 'namelist' against 'htmlfile', creates checklist: list of 
#  terms that do exist in 'htmlfile'. Returns checklist
# Uses <TD> and <td> because both exist in the htmlfiles, in different places

def namecheck(htmlfile, namelist):
    import re    
    checklist = []    
    for name in namelist:
        if not (re.search(r'<b>{foo}</b></TD><TD>(.*?)</TD>'.format(foo=name), 
                     htmlfile) == None and
                re.search(r'<b>{foo}</b></td><td>(.*?)</td>'.format(foo=name),
                     htmlfile) == None):
           checklist.append(name)
    return checklist

# Check values in 'namelist' against 'htmlfile', creates faillist: list of 
#  terms that don't exist in 'htmlfile'. Returns faillist
# Uses <TD> and <td> because both exist in the htmlfiles, in different places
 
def namefail(htmlfile, namelist):
    import re    
    faillist = []    
    for name in namelist:
        if (re.search(r'<b>{foo}</b></TD><TD>(.*?)</TD>'.format(foo=name),
                      htmlfile) == None and
            re.search(r'<b>{foo}</b></td><td>(.*?)</td>'.format(foo=name),
                      htmlfile) == None):
            faillist.append(name)
    return faillist

# Finds value of data for argument 'name' that exists in 'htmlfile' and removes 
#  html code tags. Returns value as 'data'. If data doesn't exist for 'name', 
#  returns 'Error: Reference ConvertCSV.filer - argument "name"'
# Uses <TD> and <td> because both exist in the htmlfiles, in different places

def filer(htmlfile, name):
    import re
    regex = ''
    regex1= r'<b>{foo}</b></td><td>(.*?)</td>'
    regex2= r'<b>{foo}</b></TD><TD>(.*?)</TD>'
    if re.search(regex1.format(foo=name), htmlfile) != None:
        regex = regex1
    else:
        pass
    if re.search(regex2.format(foo=name), htmlfile) != None:
        regex = regex2
    else:
        pass
    textsearch = re.search(regex.format(foo=name), htmlfile)        
    try:    
        data = textsearch.group(1)
        return data
    except:
        data = 'Error: Reference ConvertCSV.filer - argument "name"'        
        return data




       
def cleaner(entry):
    import regex
    rid_pat1 = r'<(.*?)>'
    rid_pat2 = r'a href='
    rid_pat3 = r'<br />'
    if regex.search(rid_pat1, entry) != None:
        if regex.search(rid_pat3, entry) != None:
            a = entry.rstrip(rid_pat3)
            return a
        elif regex.search(rid_pat1, entry) != None:
            b = regex.search(rid_pat1, entry).group(1).strip(rid_pat2)
            return b
        else:
            pass
    else:
        return entry
            
    