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

mat = nel.io.matlab.load('H:\Single_Day_WTrack\JS15_direct\JS15spikes01.mat')

mat = scipy.io.loadmat('H:\Single_Day_WTrack\JS15_direct\JS15spikes01.mat', 
                       struct_as_record=False, squeeze_me=True)
def load_spike(mat) :
    spikedata = []
    spiketimes = {}
    timeranges = {}
    # Spike files contain data for all epochs, tetrodes, and cells in a day
    # Some epochs have fields: ['data', 'descript', 'fields', 'depth', 'spikewidth', 'timerange']
    # but some epochs are missing 'spikewidth'
    data = mat['spikes']
    for epidx, da in enumerate(data):
        for tetidx, te in enumerate(da):
            if isinstance(te, np.ndarray):
                for cellidx, cell in enumerate(te):
                    spikedata.append({})
                    spikedata[-1]['Epoch'] = epidx
                    neuron_idx = (tetidx, cellidx)
                    
                    if (tetidx, cellidx) not in spiketimes:
                        spiketimes[(tetidx, cellidx)] = []
                        timeranges[(tetidx, cellidx)] = []
                    
                    spikedata[-1]['Tetrode'] = tetidx
                    spikedata[-1]['Cell'] = cellidx
                    if (isinstance(cell, np.ndarray)) :
                        continue # No data for this tetrode/cell combo
                        
                    timeranges[(tetidx,cellidx)].append(cell.timerange)

                    spikedata[-1].update({f: getattr(cell,f) for f in cell._fieldnames})
                    if cell.data.size == 0 :
                        spikedata[-1]['spiketimes'] = cell.data # this is an empty array
                    else :
                        if (cell.data.ndim == 1) :
                            spikedata[-1]['spiketimes'] = cell.data[0]
                            spiketimes[(tetidx,cellidx)].extend(cell.data[0])
                        else :
                            spikedata[-1]['spiketimes'] = cell.data[:,0]
                            spiketimes[(tetidx,cellidx)].extend(cell.data[:,0])


            else: # Single cell on tetrode
                spikedata.append({})
                spikedata[-1]['Epoch'] = epidx
                neuron_idx = (tetidx, 0)
                if (tetidx, cellidx) not in spiketimes:
                    spiketimes[(tetidx, cellidx)] = []
                    timeranges[(tetidx, cellidx)] = []
                    
                spikedata[-1]['Tetrode'] = tetidx
                spikedata[-1]['Cell'] = 0
                spikedata[-1].update({f: getattr(te,f) for f in te._fieldnames})
                
                timeranges[(tetidx,cellidx)].append(te.timerange)

                if te.data.size == 0 :
                    spikedata[-1]['spiketimes'] = te.data # this is an empty array
                else : 
                    if (te.data.ndim == 1) :
                        spikedata[-1]['spiketimes'] = te.data[0]
                        spiketimes[(tetidx,cellidx)].extend(te.data[0])

                    else :
                        spikedata[-1]['spiketimes'] = te.data[:,0]
                        spiketimes[(tetidx,cellidx)].extend(te.data[:,0])



    return spikedata, spiketimes, timeranges


spikedata, spiketimes, timeranges = load_spike(mat)

#get rid of any cells that do not have data
spikes = []
for dat in spikedata:
    spikedata_cell = dat
    if  len(spikedata_cell) > 3:
        spikes.append({})
        spikes[-1] = spikedata_cell
        del spikedata_cell
    else:
        del spikedata_cell
        continue
            
