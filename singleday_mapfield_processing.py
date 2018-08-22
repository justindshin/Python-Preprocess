# -*- coding: utf-8 -*-
#"""
#Created on Tue Aug 21 15:16:26 2018
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

mapmat = scipy.io.loadmat('H:\Single_Day_WTrack\JS15_direct\JS15mapfields01.mat', 
                       struct_as_record=False, squeeze_me=True)

def load_mapfield(mapmat):
    mapfielddata = []

    data = mapmat['mapfields']
    for epidx, da in enumerate(data):
        for tetidx, te in enumerate(da):
                if isinstance(te, np.ndarray):
                    for cellidx, cell in enumerate(te):
                        if cell:
                            mapfielddata.append({})
                            mapfielddata[-1]['Epoch'] = epidx
                            neuron_idx = (tetidx, cellidx)
                            mapfielddata[-1]['Tetrode'] = tetidx
                            mapfielddata[-1]['Cell'] = cellidx
                            mapfielddata[-1].update({f: getattr(cell,f) for f in cell._fieldnames})
                        else:
                            continue
                else: # Single cell on tetrode
                    mapfielddata.append({})
                    mapfielddata[-1]['Epoch'] = epidx
                    neuron_idx = (tetidx, 0)
                    mapfielddata[-1]['Tetrode'] = tetidx
                    mapfielddata[-1]['Cell'] = 0
                    mapfielddata[-1].update({f: getattr(te,f) for f in te._fieldnames})
                        
    return mapfielddata

mapfields = load_mapfield(mapmat)

