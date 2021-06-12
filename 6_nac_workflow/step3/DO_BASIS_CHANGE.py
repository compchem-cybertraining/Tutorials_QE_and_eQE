import os
import sys

# Fisrt, we add the location of the library to test to the PYTHON path
if sys.platform=="cygwin":
    from cyglibra_core import *
elif sys.platform=="linux" or sys.platform=="linux2":
    from liblibra_core import *
    

from libra_py import hpc_utils
from libra_py import data_read
from libra_py import data_outs
from libra_py import units
from libra_py import QE_methods
from libra_py.workflows.nbra import step3
#import libra_py.workflows.nbra.step2_analysis as step2a

#import numpy as np
#from matplotlib.mlab import griddata

import matplotlib.pyplot as plt   # plots
#%matplotlib inline 

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




"""
  Total number of electrons 58 => 28 alp + 28 bet
       

                                            (HOMO)  (LUMO) 
  1, 2, .. [ 20, 21, 22, 23, 24, 25, 26, 27, 28,    29   , ....    39,] 40, 41, ....


  Output matrices:

  [20, 21, ... 27, 28, 29, 30, ...  39, ] [40, 41, ... 48,         ... 59 ]



   0    1     [ 7,  8,  9,  10,]      19   20  21   [27,28, 29, 30,]  ... 39


                1   2   3    4                      -5. -6. -7. -8

"""



params = { "data_set_paths" : [os.getcwd()+"/traj1_in/"],
           "data_dim":40, "active_space":range(0,40),
           "isnap":0,  "fsnap":29,         
           "data_re_prefix" : "S_dia_ks_", "data_re_suffix" : "_re",
           "data_im_prefix" : "S_dia_ks_", "data_im_suffix" : "_im"  }
S = data_read.get_data_sets(params)

params.update({ "data_re_prefix" : "St_dia_ks_", "data_re_suffix" : "_re",
                "data_im_prefix" : "St_dia_ks_", "data_im_suffix" : "_im"  } ) 
St = data_read.get_data_sets(params)

params.update({ "data_re_prefix" : "hvib_dia_", "data_re_suffix" : "_re",
                "data_im_prefix" : "hvib_dia_", "data_im_suffix" : "_im"  } ) 
Hvib_ks = data_read.get_data_sets(params)




# Remove the previous results and temporary working directory from the previous runs
os.system("rm -r traj1_out")

# Create the new results directory
os.system("mkdir traj1_out")





params = { "SD_basis" : [ [ 7,  8, -27, -28], [7, 8, -27, -29], [7, 8, -27, -30] ],
           "SD_energy_corr" : [0.0, 0.0, 0.0],
           "CI_basis" : [ [1.0, 0.0, 0.0],
                          [0.0, 1.0, 0.0],
                          [0.0, 0.0, 1.0]
                        ],
          "output_set_paths" : [os.getcwd()+"/traj1_out/"], 
          "dt" : 1.0*units.fs2au,
          "do_orthogonalization":1,
          "do_state_reordering":2,
          "state_reordering_alpha":0.0,
          "do_phase_correction":1,
          "do_output" : 1,
          "Hvib_re_prefix":"Hvib_",  "Hvib_re_suffix":"_re",
          "Hvib_im_prefix":"Hvib_",  "Hvib_im_suffix":"_im"
         }

Hvib = step3.run(S, St, Hvib_ks, params)
