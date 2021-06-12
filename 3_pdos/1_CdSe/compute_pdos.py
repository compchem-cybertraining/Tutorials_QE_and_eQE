import sys
import cmath
import math
import os

if sys.platform=="cygwin":
    from cyglibra_core import *
elif sys.platform=="linux" or sys.platform=="linux2":
    from liblibra_core import *

import util.libutil as comn
from libra_py import pdos, data_conv

import matplotlib.pyplot as plt   # plots
#matplotlib.use('Agg')
#%matplotlib inline 

import numpy as np
#from matplotlib.mlab import griddata

plt.rc('axes', titlesize=24)      # fontsize of the axes title
plt.rc('axes', labelsize=20)      # fontsize of the x and y labels
plt.rc('legend', fontsize=20)     # legend fontsize
plt.rc('xtick', labelsize=16)    # fontsize of the tick labels
plt.rc('ytick', labelsize=16)    # fontsize of the tick labels

plt.rc('figure.subplot', left=0.2)
plt.rc('figure.subplot', right=0.95)
plt.rc('figure.subplot', bottom=0.13)
plt.rc('figure.subplot', top=0.88)

colors = {}

colors.update({"11": "#8b1a0e"})  # red       
colors.update({"12": "#FF4500"})  # orangered 
colors.update({"13": "#B22222"})  # firebrick 
colors.update({"14": "#DC143C"})  # crimson   

colors.update({"21": "#5e9c36"})  # green
colors.update({"22": "#006400"})  # darkgreen  
colors.update({"23": "#228B22"})  # forestgreen
colors.update({"24": "#808000"})  # olive      

colors.update({"31": "#8A2BE2"})  # blueviolet
colors.update({"32": "#00008B"})  # darkblue  

colors.update({"41": "#2F4F4F"})  # darkslategray

clrs_index = ["11", "21", "31", "41", "12", "22", "32", "13","23", "14", "24"]



E_f = 2.1608
Cd_p = [["p"], [1, 2], ["Cd"] ]
Cd_d = [["d"], [1, 2], ["Cd"] ]
Se_p = [["p"], [3, 4], ["Se"] ]
Se_d = [["d"], [3, 4], ["Se"] ]
projections = [ Cd_p, Cd_d, Se_p, Se_d ]

E, pdosa, pdosb = pdos.QE_pdos("pdos/x.pdos_atm#", -10.0, 10.0, 0.1, projections,\
                               E_f, "pdos_", 1, 0.01, 0.1, nspin=2)



e_grid = data_conv.MATRIX2nparray(E)
proja = data_conv.MATRIX2nparray(pdosa)
projb = data_conv.MATRIX2nparray(pdosb)

print(e_grid.shape, proja.shape, projb.shape)



def plot(_energy, _pdosa, _pdosb):
    
    plt.rc('axes', titlesize=18)      # fontsize of the axes title
    plt.rc('axes', labelsize=18)      # fontsize of the x and y labels
    plt.rc('legend', fontsize=12)     # legend fontsize
    plt.rc('xtick', labelsize=18)     # fontsize of the tick labels
    plt.rc('ytick', labelsize=18)     # fontsize of the tick labels
    
    plt.ylim(-5.0, 5.0)
    plt.xlim(-5.0, 7.0)

    
    #======== Now lets plot what we have computed ===========
    plt.figure(1, figsize=(36, 24), dpi=300, frameon=False)
    
    lw = 3 
    plt.title('CdSe pDOS')
    plt.xlabel('$E - E_f, eV$')
    plt.ylabel('pDOS, 1/eV')    
    plt.plot(_energy[:,0], _pdosa[:, 0], label='Cd(p)', linewidth=lw, color = colors["11"]) 
    plt.plot(_energy[:,0], _pdosa[:, 1], label='Cd(d)', linewidth=lw, color = colors["21"]) 
    plt.plot(_energy[:,0], _pdosa[:, 2], label='Se(p)', linewidth=lw, color = colors["31"]) 
    plt.plot(_energy[:,0], _pdosa[:, 3], label='Se(d)', linewidth=lw, color = colors["41"])     
    
    plt.plot(_energy[:,0], -_pdosb[:, 0], linewidth=lw, color = colors["11"]) 
    plt.plot(_energy[:,0], -_pdosb[:, 1], linewidth=lw, color = colors["21"]) 
    plt.plot(_energy[:,0], -_pdosb[:, 2], linewidth=lw, color = colors["31"]) 
    plt.plot(_energy[:,0], -_pdosb[:, 3], linewidth=lw, color = colors["41"])     
    plt.legend()       
            
    plt.tight_layout()
    
    plt.savefig("pdos.png")        
    #plt.show()
    
    plt.close()



plot(e_grid, proja, projb)


