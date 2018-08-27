# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:47:11 2018

@author: jdshin
"""

import numpy as np
import scipy.io
import nelpy as nel
import nelpy.plotting as npl

# assume default aesthetics
npl.setup()

def load_pos(matfile, animal):
    mat = scipy.io.loadmat('H:\Single_Day_WTrack\JS15_direct\JS15pos01.mat', 
                       struct_as_record=False, squeeze_me=True)
    matdata = []
    
    data = mat[]
    for epidx, ep in enumerate(data):
            if isinstance(data, np.ndarray):
                posdata.append({})
                posdata[-1]['Epoch'] = epidx
                posdata[-1].update({f: getattr(ep,f) for f in ep._fieldnames})

    return posdata

pos = load_pos(posmat)