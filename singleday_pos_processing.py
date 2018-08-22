#Extracts position for each epoch from .mat files generated from Jadhav lab pipeline

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import struct
import scipy.io
import nelpy as nel
import nelpy.io
import nelpy.plotting as npl

# assume default aesthetics
npl.setup()

posmat = nel.io.matlab.load('H:\Single_Day_WTrack\JS15_direct\JS15pos01.mat')

posmat = scipy.io.loadmat('H:\Single_Day_WTrack\JS15_direct\JS15pos01.mat', 
                       struct_as_record=False, squeeze_me=True)
def load_pos(pos) :
    posdata = []
    
    data = posmat['pos']
    for epidx, ep in enumerate(data):
            if isinstance(data, np.ndarray):
                posdata.append({})
                posdata[-1]['Epoch'] = epidx
                posdata[-1].update({f: getattr(ep,f) for f in ep._fieldnames})

    return posdata

pos = load_pos(posmat)