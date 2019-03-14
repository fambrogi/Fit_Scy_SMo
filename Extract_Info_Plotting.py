import os,sys
import matplotlib
matplotlib.use('Agg')
from matplotlib  import cm
from itertools import izip
from matplotlib import ticker
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import argparse
import numpy as np

min_r = 0.0
max_r = 1.0
min_Chi2 = 80

pref = 'minRvalue_'+ str(min_r) + '_MAXrValue_' + str(max_r) +'_minXi2_' + str(min_Chi2)



""" Some Pretty Labels """
Glu_M     = r'$m_{\tilde g}$ [GeV]'
Neu_M     = r'$m_{\tilde{\chi}_1 ^0 }$ [GeV]'
Neu2_M     = r'$m_{\tilde{\chi}_2 ^0 }$ [GeV]'

Ch1_M     = r'$m_{\tilde \chi_1 ^{\pm} }$ [GeV]'
Sq_M = 'min(' + r'$ m_{\tilde q }$) [GeV]'
Slep_M    = r'$m_{\tilde l }$ [GeV]'
rValue    = r'SModelS $r =\frac{\sigma_{Theo}}{\sigma_{UL}}$'
ScyXi2    = r'ScyNet $\chi ^2$'

Weight = r'$ w = \sigma \times BR $'
 

""" Selects the results based on SModelS minimum rValue 
        Dic = { 'Glu': []  , 'Neu1': [] , 'Neu2': [] , 'Ch1': [] , 'Slep': []  , 'Sq': []  , 
        'ScyChi2': [] , 'rValue': [] , 
        'Miss_Topo_Tx': [] , 'Miss_Topo_Bra':[], 'Miss_Con_Bra':[] , } """


### Turn Results into a class!!!!
def Select_Results(min_r='', max_r = '', min_xi = '', max_xi = ''):
    RESULTS = np.load('Numpys/ScyNet_Res.npy').item()
    Neu = RESULTS['Neu1']
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
     
   
        #print 'the r value is ', r
        SLEP.append(Slep[num])
        NEU.append(Neu[num])
        R.append(r)
        GLU.append(Glu[num])
        SQ.append(Sq[num])
        CH1.append(Ch1[num])
        NEU2.append(Neu[num])
        XI2.append(xi2[num])
        #print Miss_Topo_Bra[num] , Miss_Topo_Tx[num] , Miss_Con_Bra[num] 
        MISS_TOPO_BRA.append(Miss_Topo_Bra[num])
        MISS_TOPO_TX .append(Miss_Topo_Tx[num])
        MISS_CON_BRA .append(Miss_Con_Bra[num])
        MISS_TOPO_W  .append(Miss_Topo_W[num])
        MISS_CON_W   .append(Miss_Con_W[num])

    return NEU,SLEP,NEU2,CH1,GLU,SQ,     R,XI2,  MISS_TOPO_BRA,MISS_TOPO_TX,MISS_TOPO_W, MISS_CON_BRA, MISS_CON_W




