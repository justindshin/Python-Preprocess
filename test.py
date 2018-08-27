# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:54:25 2018

@author: jdshin
"""
#spikearray = []
#for spk in spikes:
#    spktm = spk['data'][:,0]
#    spikearray.append({})
#    spikearray[-1] = spktm
#    del spktm
#    
spikearray2 = []
for spk in spikes:
    spktm = spk['data'][:,0]
    spikearray2.append(spktm)
    del spktm
        