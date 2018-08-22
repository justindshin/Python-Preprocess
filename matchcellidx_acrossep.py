# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:07:46 2018

@author: jdshin
"""
#Find cells that were tracked aver all epochs specified (need to make specification clearer)
#Set up to use epoch 1 indices as template to match cells
matchidx = []
for x in spikes:
    if x['Epoch'] == 1:
        cell = x['Cell']
        tet = x['Tetrode'] 
        matchidx.append({})
        matchidx[-1]['Cell'] = cell
        matchidx[-1]['Tetrode'] = tet

cellidx=[]        
for match in matchidx:
    c = match['Cell']
    t = match['Tetrode']
    idx = [t, c]
    cellidx.append(idx)
    cellidx.sort()
    
eparray = [1]  
allep_cellidx = []
for ep in eparray: 
    for c in cellidx:
        cellinep_count = []
        for sp in spikes:
            if sp['Tetrode'] == c[0] and sp['Cell'] == c[1]:
                cellinep_count.append(sp)
        if len(cellinep_count) == 8: #dirty way to specify number of epochs to match over
            allep_cellidx.append(c)
             
#Need to incorporate PFC and HPC filters and FR filter for HPC to exclude interneurons       