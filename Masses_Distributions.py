B""" Module for plotting the masses distributions of the points 
    (no analysis on rvalues 
    
    To do: implement masses differences in the results file for easyness?
    
    """

import os,sys
import numpy as np
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec

dic = np.load('Numpys/ScyNet_Res.npy').item()

# Keys: dict_keys(['ScyChi2', 'Miss_Con_W', 'Sq', 'Ch1', 'Ch2', 'Miss_Con_Bra', 'Miss_Topo_Tx', 'Miss_Topo_Bra', 
#'Glu', 'rValue', 'Miss_Topo_W', 'Slep', 'Neu1', 'Neu2'])

print('The keys are: ', dic.keys() )

def List_Sorter(L1, L2, L3,order=True):
    # first entry is the color code
    sorted_lists = sorted(zip(L1, L2, L3), reverse=order, key=lambda x: x[0])
    L1s, L2s, L3s = [[x[i] for x in sorted_lists] for i in range(3)]
    return L1s, L2s, L3s


Q = dic['Sq']
B = dic['Sb1']
T = dic['St1']
G = dic['Glu']

N1 = dic['Neu1']
N2 = dic['Neu2']
C  = dic['Ch1']
SL = dic['Slep']

keys = dic.keys()

diff_N2_N1 = []
for n1,n2 in zip(N1,N2):
    diff_N2_N1.append(n2-n1)
    
diff_C_N1 = []
for c,n in zip(C,N1):
    diff_C_N1.append(c-n1)    

diff_C_N2 = []
for c,n2 in zip(C,N2):
    diff_C_N2.append( abs(n2)-abs(c) )


bins = 50
fnt_size = 13
histtype = 'stepfilled'
fill = True
alpha = 0.5


'''
# COLORED
plt.text(2100,2800, 'All Scanned Points' , fontsize = fnt_size)
plt.hist(Q, bins = bins , histtype = histtype, fill = fill,  color = 'orange'     , label = r'$m_{\tilde q}$'   , alpha = alpha+0.2 , edgecolor = 'orange' )
plt.hist(T, bins = bins , histtype = histtype, fill = fill,  color = 'blue'       , label = r'$m_{\tilde t_1}$' , alpha = alpha+0.2 , edgecolor = 'navy'   )
plt.hist(B, bins = bins , histtype = histtype, fill = fill,  color = 'cyan'       , label = r'$m_{\tilde b_1}$' , alpha = alpha     , edgecolor = 'cyan')
plt.hist(G, bins = bins , histtype = histtype, fill = fill,  color = 'red'        , label = r'$m_{\tilde g}$'   , alpha = alpha     , edgecolor = 'red')

plt.legend(loc = 'upper right' , fontsize = fnt_size -2 , ncol = 2)

plt.xlabel('Mass [GeV]', fontsize = fnt_size)
plt.axis([2000,5000,0,3000])

#plt.label('Mass [GeV]', fontsize = fnt_size)
plt.savefig('PLOTS/Masses/Coloured.png' , bbox_inches='tight' , dpi = 200)
plt.close()

# EW
#plt.text(50,3700, 'All Scanned Points' , fontsize = fnt_size)
plt.hist(N1, bins = bins , histtype = histtype, fill = fill,  color = 'lightgray'  , label = r'$m_{\tilde \chi _1 ^{0}} }$'      , alpha = alpha+0.2 , edgecolor = 'gray' )
plt.hist(N2, bins = bins , histtype = histtype, fill = fill,  color = 'pink'       , label = r'$m_{\tilde \chi _2 ^{0}} $'       , alpha = alpha+0.2 , edgecolor = 'magenta'   )
plt.hist(C,  bins = bins , histtype = histtype, fill = fill,  color = 'mediumslateblue', label = r'$m_{\tilde \chi _1 ^{\pm}} $' , alpha = alpha     , edgecolor = 'blue')
plt.hist(SL, bins = bins , histtype = histtype, fill = fill,  color = 'dodgerblue' , label = r'$m_{\tilde l}$'                   , alpha = alpha     , edgecolor = 'navy')

plt.legend(loc = 'upper right' , fontsize = fnt_size -2 , ncol = 2)

plt.xlabel('Mass [GeV]', fontsize = fnt_size)
plt.axis([0,700,0,4000])

#plt.label('Mass [GeV]', fontsize = fnt_size)
plt.savefig('PLOTS/Masses/EW.png' , bbox_inches='tight' , dpi = 200)
plt.close()

'''

# Differences


z,x,y  = List_Sorter(diff_C_N2, diff_N2_N1 , diff_C_N1, order=False)


plt.scatter( x, y, c = z , cmap = 'jet' , s = 6)
cbar = plt.colorbar()
cbar.set_label(r'$m_{\tilde \chi _2 ^{0}}   - m_{\tilde \chi _1 ^{\pm}}   $   [GeV]', size = fnt_size)

#plt.legend(loc = 'upper right' , fontsize = fnt_size -2 , ncol = 2)

plt.grid(color = 'lightgray' , linestyle = ':')
plt.xlabel(r'$m_{\tilde \chi _2 ^{0}}   - m_{\tilde \chi _1 ^{0}}   $   [GeV]', fontsize = fnt_size)
plt.ylabel(r'$m_{\tilde \chi _1 ^{\pm}} - m_{\tilde \chi _1 ^{0}}   $   [GeV]', fontsize = fnt_size)

plt.axis([0,700,0,700])
#plt.label('Mass [GeV]', fontsize = fnt_size)
plt.savefig('PLOTS/Masses/Diff_EW.png' , bbox_inches='tight' , dpi = 200)
plt.close()
