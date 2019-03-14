B"""
   Author: Ambrogi Federico
           federico.ambrogi@univie.ac.at

   Module for analysing the output root files
   and plotting the weights of the missing TxNames or missing models 
"""

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

from Extract_Info_Plotting import *


'''
""" Selects the results based on SModelS minimum rValue """


def Select_Results(results = 'Numpy/ScyNet_Res.py', 'min_r = 100, max_r = 1000, min_chi = 100, debug= False):
""" Selects the results based:

    Args:
         results: numpy files, converted from the root file, by the script 
    min SModelS r_value
    max SModelS r_value
    min ScyNet chi2

    returns a dictionary with the information of particles masses and values """


    RESULTS = np.load(results).item()
    Neu = RESULTS['Neu1']
    Slep = RESULTS['Slep']
    Neu2 = RESULTS['Neu2']
    Ch1  = RESULTS['Ch1']
    rVal = RESULTS['rValue']
    Glu  = RESULTS['Glu']
    Sq   = RESULTS['Sq']
    xi2  = RESULTS['ScyChi2']

    NEU,SLEP,NEU2,CH1,GLU,SQ,R,XI2 = [],[],[],[],[],[],[],[]

    ### Choose a number of points (all or 10 for debugging)
    if debug == True: 
       num_points = 10
    elif debug == False:
       num_points = range(len(Neu))

    for num in num_points:
        
        r     = rVal[num]
        chi_2 = xi2[num]  
        if r < min_r : continue       # cut on the SMo rvalue
        if r > max_r : continue
        if chi_2 < min_chi : continue

        if debug: print 'the min rvalue and the min chi_2 are:  *** ', r , ' ' , chi_2

        SLEP.append(Slep[num])
        NEU.append(Neu[num])
        R.append(r)
        GLU.append(Glu[num])
        SQ.append(Sq[num])
        CH1.append(Ch1[num])
        NEU2.append(Neu[num])
        XI2.append(xi2[num])
    return NEU,SLEP,NEU2,CH1,GLU,SQ,R,XI2
'''

min_r = 0.9
min_chi = 40
max_r = 50
max_chi = 200
NEU,SLEP,NEU2,CH1,GLU,SQ, R,XI2,  MISS_TOPO_BRA,MISS_TOPO_TX,MISS_TOPO_W, MISS_CON_BRA,MISS_CON_W,dic = Select_Results(min_r = min_r, min_xi = min_chi, max_r = max_r, max_xi = max_chi, debug= True)


def Plane_Prop(plane):
    Max_Neu = 400

    Slep_Neu = { 'xmin': 0 , 'xmax': 800 ,
                    'ymin': 0 , 'ymax': Max_Neu ,
                    'x_lab_pos:': 100 , 'y_lab_pos': 2800 ,
                    'xlab': Slep_M , 'ylab': Neu_M }
   
    Ch1_Neu     = { 'xmin': 0 ,'xmax':700 ,
                    'ymin': 0 ,'ymax': Max_Neu ,
                    'x_lab_pos:': 100 , 'y_lab_pos': 2800 ,
                    'xlab': Ch1_M , 'ylab': Neu_M }
   
    Glu_Neu     = { 'xmin': 2300 ,'xmax':3500 ,
                    'ymin': 0 ,'ymax': Max_Neu ,
                    'x_lab_pos:': 100 , 'y_lab_pos': 2800 ,
                    'xlab': Glu_M , 'ylab': Neu_M }

    Sq_Neu      = { 'xmin': 2300 ,'xmax':3500 ,
                    'ymin': 0 ,'ymax': Max_Neu ,
                    'x_lab_pos:': 100 , 'y_lab_pos': 2800 ,
                    'xlab': Sq_M , 'ylab': Neu_M  }
 
    if    plane == 'Slep_Neu':
       return Slep_Neu, SLEP, NEU, R , XI2
    elif  plane == 'Ch1_Neu':
        return Ch1_Neu, CH1, NEU, R , XI2
    elif  plane == 'Glu_Neu':
        return Glu_Neu, GLU, NEU, R , XI2
    elif  plane == 'Sq_Neu':
        return Sq_Neu, SQ, NEU, R , XI2


def Color_Bar(plt , size = '' , bins = '' , title = '' ):
    cbar = plt.colorbar() 
    cbar.set_label( title , rotation = 90, fontsize = size)
    tick_locator = ticker.MaxNLocator(nbins=bins)
    cbar.locator = tick_locator
    cbar.update_ticks()

def Plot_Properties(Dic_Prop):
    plt.xlabel(Dic_Prop['xlab'] , fontsize = FONTSIZE)                                                                                                                      
    plt.ylabel(Dic_Prop['ylab'] , fontsize = FONTSIZE) 
    plt.grid()
    plt.axis([ Dic_Prop['xmin'], Dic_Prop['xmax'], Dic_Prop['ymin'] , Dic_Prop['ymax'] ])
    

Planes = ['Slep_Neu', 'Ch1_Neu', 'Glu_Neu', 'Sq_Neu']

Marker_Size = 10
BINS = 5
FONTSIZE = 20
REV = False
VMAX = 5

'''
""" SModelS rValues """
for P in Planes:
    Dic_Prop , x , y , z , u = Plane_Prop(P)
    sorted_lists = sorted(izip(x , y, z), reverse=REV, key=lambda x: x[2])                                                                                                        
    X,Y,Z = [[x[i] for x in sorted_lists] for i in range(3)] 
    plt.scatter(-100,-100, color = 'gray', label = r'Only rValue > 0.9: ' + str(len(X)) )
    plt.scatter(X, Y, c =  Z , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none' , vmin=1, vmax = 5 )
    Color_Bar(plt , size = FONTSIZE , bins = BINS , title = rValue )
    Plot_Properties(Dic_Prop)
    plt.legend(loc ='upper right', fontsize = FONTSIZE-9, fancybox = True)
    plt.savefig(P + '_rValue_all.pdf', bbox_inches='tight')
    plt.savefig('/afs/hephy.at/user/f/fambrogi/www/Fittino/' + P + '_rValue_all.pdf', bbox_inches='tight' )
    plt.close()
'''

""" SModelS rValues """
BINS = 6
VMAX = 120
for P in Planes:
    Dic_Prop , x , y , z , u = Plane_Prop(P)
    sorted_lists = sorted(izip(x , y, u), reverse=REV, key=lambda x: x[2])
    X,Y,Z = [[x[i] for x in sorted_lists] for i in range(3)]
    plt.scatter(-100,-100, color = 'gray', label = r'Only rValue > 0.9: ' + str(len(X)) )
    plt.scatter(X, Y, c =  Z , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none' , vmin=1, vmax = VMAX )
    Color_Bar(plt , size = FONTSIZE , bins = BINS , title = ScyXi2 )
    Plot_Properties(Dic_Prop)
    plt.legend(loc ='upper right', fontsize = FONTSIZE-9, fancybox = True)
    plt.savefig(P + '_ScyNetChi2_'+str(min_r)+'.pdf', bbox_inches='tight')
    plt.savefig('/afs/hephy.at/user/f/fambrogi/www/Fittino/' + P + '_ScyNetChi2_'+str(min_r)+'.pdf', bbox_inches='tight' )
    plt.close()





'''
def Axis_Properties(WHAT, plt, XLABEL='x', xmin=0, XMAX=1000, YLABEL='y', ymin=0, YMAX= 1000, FONTSIZE=18, COSA = 'what is this', ana = '' , txt_1 = '', lab_x = 1 , lab_y = 1):
    
    color = 'red'
    plt.xlabel(XLABEL , fontsize = FONTSIZE)
    plt.ylabel(YLABEL , fontsize = FONTSIZE)
    plt.axis([xmin, XMAX, ymin , YMAX])
    plt.text(lab_x, lab_y  , WHAT + '-like LSP'  , {'color':color , 'fontsize': FONTSIZE-4} , bbox=dict(edgecolor='white',facecolor='white'))
    #plt.text(lab_x ,lab_y - YMAX/13  , COSA        , {'color':'black' , 'fontsize': FONTSIZE-4} , bbox=dict(edgecolor='black',facecolor='white'))
    plt.text(lab_x ,lab_y-YMAX/17 , txt_1      , {'color':'black' , 'fontsize': FONTSIZE-4} , bbox=dict(edgecolor='white',facecolor='white'))

def Scatter_Plot(x='', y = '' , xlabel = '', ylabel = '' , z = '', zlabel = '' , ana='' , txt_1 = '' , text = 'ciao', WHAT='' , suff = 'something' , place = '' , bins= ''):

    LAB_X = place['lab_x']    
    LAB_Y = place['lab_y']
    ymax =  place['y_max']
    XMAX = place['x_max']
    sorted_lists = sorted(izip(x , y, z), reverse=REV, key=lambda x: x[2])
    X,Y,Z = [[x[i] for x in sorted_lists] for i in range(3)]
    plt.scatter(X, Y, c =  Z , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none' , vmin=min, vmax = MAX )
    Axis_Properties(WHAT,plt, XLABEL= xlabel, xmin=200, XMAX=XMAX, YLABEL = ylabel, ymin=0, YMAX= ymax, FONTSIZE=fontsize+3 , ana = ana, txt_1 = text,
                    lab_x = LAB_X , lab_y = LAB_Y)

    Color_Bar(plt , size = 18 , bins = bins , title = zlabel)
    plt.grid()
    plt.savefig('PLOTS/'+ WHAT + '_rValus_'+suff+'.png', dpi = 250, bbox_inches='tight' )

#/afs/hephy.at/user/f/fambrogi/www/TGQ_Paper    
    plt.savefig('/afs/hephy.at/user/f/fambrogi/www/TGQ_Paper/'+ WHAT + '_rValus_'+suff+'.png', dpi = 250, bbox_inches='tight' )
    plt.close()




# Positions of labels
PLACE_Glu_SqLSP = {'lab_y':130 , 'y_max':150, 'x_max': 4000 , 'lab_x':300 }

BINS = 10
min , MAX = 1, 10
REV = False
Marker_Size = 8
xmax, ymax = 1500 , 1000
fontsize = 19

Glu_M     = r'$m_{\tilde g}$ [GeV]'   
Neu_M     = r'$m_{\tilde{\chi}_1 ^0 }$ [GeV]'
Ch1_M     = r'$m_{\tilde \chi_1 ^{\pm} }$ [GeV]'
Light_S_M = 'min(' + r'$ m_{\tilde q }$) [GeV]'
rValue    = r'SModelS $r =\frac{\sigma_{Theo}}{\sigma_{UL}}$'

REV = True
label =  r'SModelS $\frac{Best \ rvalue}{Total \ rvalue}$'
'''


