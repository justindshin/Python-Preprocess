# -*- coding: utf-8 -*-
#"""
#Created on Tue Aug 21 12:51:54 2018
#
#@author: jdshin
#"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import struct
import scipy.io
import nelpy as nel
import nelpy.io
import nelpy.plotting as npl

#linmat = nel.io.matlab.load('H:\Single_Day_WTrack\JS15_direct\JS15linfields01.mat')
linmat = scipy.io.loadmat('H:\Single_Day_WTrack\JS15_direct\JS15linfields01.mat', 
                       struct_as_record=False, squeeze_me=True)

def load_linfield(linmat):
    linfielddata = []

    data = linmat['linfields']
    for epidx, da in enumerate(data):
        for tetidx, te in enumerate(da): 
            if isinstance(te, np.ndarray):
                for cellidx, cell in enumerate(te):
                    if len(cell) < 20:
                        linfielddata.append({})
                        linfielddata[-1]['Epoch'] = epidx
                        neuron_idx = (tetidx, cellidx)
                        linfielddata[-1]['Tetrode'] = tetidx
                        linfielddata[-1]['Cell'] = cellidx
                        if len(cell) == 4:
                            outl = cell[0]; inl = cell[1]; outr = cell[2]; inr = cell[3] 
                            linfielddata[-1].update({'outleft':outl})
                            linfielddata[-1].update({'inleft':inl})
                            linfielddata[-1].update({'outright':outr})
                            linfielddata[-1].update({'inright':inr})
                    else:  
                         if cellidx == 0:
                            linfielddata.append({})
                            linfielddata[-1]['Epoch'] = epidx
                            neuron_idx = (tetidx, cellidx)
                            linfielddata[-1]['Tetrode'] = tetidx
                            linfielddata[-1]['Cell'] = cellidx
                            outl = te[0]; inl = te[1]; outr = te[2]; inr = te[3] 
                            linfielddata[-1].update({'outleft':outl})
                            linfielddata[-1].update({'inleft':inl})
                            linfielddata[-1].update({'outright':outr})
                            linfielddata[-1].update({'inright':inr})
                         else:
                            continue
                    
    return linfielddata

lfields = load_linfield(linmat)

#get rid of any cells that do not have linfield data
linfields = []
for dat in lfields:
    lfielddata_cell = dat
    if  len(lfielddata_cell) > 3:
        linfields.append({})
        linfields[-1] = lfielddata_cell
        del lfielddata_cell
    else:
        del lfielddata_cell
        continue
           
            
   