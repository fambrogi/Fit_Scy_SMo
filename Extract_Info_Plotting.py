""" Auxilliary module with functionalities to extract info and plotting """

import os,sys
import matplotlib
matplotlib.use('Agg')
from matplotlib  import cm
from matplotlib import ticker
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import argparse
import numpy as np





""" Some Pretty Labels """
Glu_M     = r'$m_{\tilde g}$ [GeV]'
Neu_M     = r'$m_{\tilde{\chi}_1 ^0 }$ [GeV]'
Neu2_M     = r'$m_{\tilde{\chi}_2 ^0 }$ [GeV]'

Ch1_M     = r'$m_{\tilde \chi_1 ^{\pm} }$ [GeV]'
Sq_M = 'min(' + r'$ m_{\tilde q }$) [GeV]'
Slep_M    = r'$m_{\tilde l }$ [GeV]'
rValue    = r'SModelS $r =\frac{\sigma_{Theo}}{\sigma_{UL}}$'
ScyXi2    = r'ScyNet $\chi ^2$'


DiffN2N1_M = r'$m_{\tilde{\chi}_2 ^0} - m_{\tilde{\chi}_1 ^0}   $ [GeV]'


Weight = r'$ w = \sigma \times BR \ [fb] $'
 

""" Selects the results based on SModelS minimum rValue
    
    Structure of the dictionary in the RESULTS file:
    Dic = { 'Glu': []  , 'Neu1': [] , 'Neu2': [] , 'Ch1': [] , 'Slep': []  , 'Sq': []  , 
            'ScyChi2': [] , 'rValue': [] , 
            'Miss_Topo_Tx': [] , 'Miss_Topo_Bra':[], 'Miss_Con_Bra':[] , } 

    Miss_Topo_Tx   is weight 
    Miss_Topo_Tx   is
    Miss_Topo_Bra  is 

"""


### Turn Results into a class!!!!
def Select_Results(results = 'Numpys/ScyNet_Res.npy', min_r='', max_r = '', min_xi = '', max_xi = '', debug = True):
    RESULTS = np.load(results).item()
    Neu  = RESULTS['Neu1']
    Slep = RESULTS['Slep']
    Neu2 = RESULTS['Neu2']
    Ch1  = RESULTS['Ch1']
    rVal = RESULTS['rValue']
    Glu  = RESULTS['Glu']
    Sq   = RESULTS['Sq']
    xi2  = RESULTS['ScyChi2']
    Miss_Topo_Tx , Miss_Topo_Bra , Miss_Con_Bra = RESULTS['Miss_Topo_Tx'], RESULTS['Miss_Topo_Bra'], RESULTS['Miss_Con_Bra']
    Miss_Topo_W , Miss_Con_W = RESULTS['Miss_Topo_W'] , RESULTS['Miss_Con_W']

    NEU,SLEP,NEU2,CH1,GLU,SQ,R,XI2 = [],[],[],[],[],[],[],[]
    MISS_TOPO_BRA , MISS_TOPO_TX , MISS_CON_BRA , MISS_TOPO_W, MISS_CON_W = [],[],[], [],[]

    for num in range(len(Neu)):

        r = rVal[num]
        xi = xi2[num]
  
        if r >= min_r and r <= max_r and xi > min_xi and xi < max_xi:
            SLEP.append(Slep[num])
            NEU.append(Neu[num])
            R.append(r)
            GLU.append(Glu[num])
            SQ.append(Sq[num])
            CH1.append(Ch1[num])
            NEU2.append(Neu2[num])
            XI2.append(xi2[num])
            MISS_TOPO_BRA.append(Miss_Topo_Bra[num])
            MISS_TOPO_TX .append(Miss_Topo_Tx[num])
            MISS_CON_BRA .append(Miss_Con_Bra[num])
            MISS_TOPO_W  .append(Miss_Topo_W[num])
            MISS_CON_W   .append(Miss_Con_W[num])
            
#            if (Miss_Con_W[num]  > 5 or Miss_Topo_W[num] > 5):
#                print('bracket, weight', Miss_Con_Bra[num] , Miss_Con_W[num] )
#                
#                print('topo, weight', Miss_Topo_Tx[num] , Miss_Topo_W[num] )
#                input('')
            
            
    dic = {'Neu'         : NEU  , 
           'Neu2'        : NEU2 , 
           'Slep'        : SLEP , 
           'Sq'          : SQ,
           'Glu'         : GLU, 
           'Ch1'         : CH1  , 
           'rValue'      : R    , 
           'chi2'        : XI2  ,
           'MissTopoBra' : MISS_TOPO_BRA ,
           'MissTopoTx'  : MISS_TOPO_TX  ,
           'MissTopoW'   : MISS_TOPO_W   ,
           'MissConBra'  : MISS_CON_BRA  ,
           'MissConW'  : MISS_CON_W }

    return dic 




#dic  = Select_Results(results = 'Numpys/ScyNet_Res.npy', min_r=0, max_r = 10, min_xi = 20, max_xi = 1000, debug = True)
