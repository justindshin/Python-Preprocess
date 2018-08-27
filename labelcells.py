# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:34:51 2018

@author: jdshin
"""

#Specify tetrode metadata - remember 0 indexing
#JS15 metadata
ca1tet = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20, 21, 22, 23, 24, 25]
pfctet =[0, 1, 2, 3, 14, 15, 16, 17, 18, 19, 27, 28, 29, 30, 31]

#riptet = []

#Split into separate dics
ca1_spikes = []
for tet in ca1tet:
    for t, cell in enumerate(spikes):
        if cell['Tetrode'] == tet:
            cell['Area'] = 'CA1'
            if cell['meanrate'] > 7:
                cell['tag'] = 'CA1int'
                ca1_spikes.append({})
                ca1_spikes[-1] = cell
                spikes[t]['tag'] = 'CA1int'
                spikes[t]['Area'] = 'CA1'
            else:
                cell['tag'] = 'CA1pyr'
                ca1_spikes.append({})
                ca1_spikes[-1] = cell 
                spikes[t]['tag'] = 'CA1pyr'
                spikes[t]['Area'] = 'CA1'
        else:
            continue
        
pfc_spikes = []
for tet2 in pfctet:
    for t, cell in enumerate(spikes):
        if cell['Tetrode'] == tet2:
            cell['Area'] = 'PFC'
            pfc_spikes.append({})
            pfc_spikes[-1] = cell
            spikes[t]['Area'] = 'PFC'
        else:
            continue
        
       