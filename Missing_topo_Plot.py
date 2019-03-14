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
#
#
#
# Extracting Results
NEU,SLEP,NEU2,CH1,GLU,SQ,  R,XI2,MISS_TOPO_BRA,MISS_TOPO_TX,MISS_TOPO_W, MISS_CON_BRA, MISS_CON_W  = Select_Results(min_r = min_r , max_r = max_r, min_xi= min_Chi2, max_xi= 10000)


""" Counting Missing topo """
#print  MISS_TOPO_BRA, MISS_TOPO_TX, MISS_CON_BRA
#raw_input('check lists')
Set_Miss_Topo_Tx = list(set(MISS_TOPO_TX))
Set_Miss_Con_Bra = list(set(MISS_CON_BRA))

print 'Complete set of Missing TxNames'  , Set_Miss_Topo_Tx
print 'Complete set of Missing Brackets' , Set_Miss_Con_Bra

Dic_Tx , Dic_Bra = {} , {}
for N in Set_Miss_Topo_Tx:
    #print N , '-', MISS_TOPO_TX.count(N)
    Dic_Tx[N] = MISS_TOPO_TX.count(N)

for N in Set_Miss_Con_Bra:
    #print N , '-', MISS_CON_BRA.count(N)
    Dic_Bra[N] = MISS_CON_BRA.count(N)

sorted_Dic_Tx  = sorted(Dic_Tx.items()   , key=lambda x: x[1])
sorted_Dic_Bra = sorted(Dic_Bra.items()  , key=lambda x: x[1])

print 'Sorted TxNames entries: **** \n'
for i in sorted_Dic_Tx:
    print i

print 'Sorted Brackets entries: **** \n'
for i in sorted_Dic_Bra:
    print i

#raw_input()

# This must be improved
def Plane_Prop(plane):
    Max_Neu = 400
    Slep_Neu = {    'X': SLEP, 'Y':NEU, 
                    'xmin': 0 , 'xmax': 800 ,
                    'ymin': 0 , 'ymax': Max_Neu ,
                    'x_lab_pos': 30 , 'y_lab_pos': 350 ,
                    'xlab': Slep_M , 'ylab': Neu_M }
   
    Ch1_Neu     = { 'X':CH1 , 'Y': NEU,
                    'xmin': 0 ,'xmax':700 ,
                    'ymin': 0 ,'ymax': Max_Neu ,
                    'x_lab_pos': 30 , 'y_lab_pos': 350 ,
                    'xlab': Ch1_M , 'ylab': Neu_M }
   
    Glu_Neu     = { 'X':GLU , 'Y': NEU,
                    'xmin': 2300 ,'xmax':3500 ,
                    'ymin': 0 ,'ymax': Max_Neu ,
                    'x_lab_pos': 2350 , 'y_lab_pos': 350 ,
                    'xlab': Glu_M , 'ylab': Neu_M }


    Sq_Neu      = { 'X': SQ, 'Y': NEU ,
                    'xmin': 2300 ,'xmax':3500 ,
                    'ymin': 0 ,'ymax': Max_Neu ,
                    'x_lab_pos': 2350 , 'y_lab_pos': 350 ,
                    'xlab': Sq_M , 'ylab': Neu_M  }
 
    Neu2_Neu      = { 'X': NEU2, 'Y': NEU ,
                    'xmin': 0 ,'xmax': 700 ,
                    'ymin': 0 ,'ymax': Max_Neu ,
                    'x_lab_pos': 30, 'y_lab_pos': 340 ,
                    'xlab': Neu2_M , 'ylab': Neu_M  }


    if    plane == 'Slep_Neu':
       return Slep_Neu
    elif  plane == 'Ch1_Neu':
        return Ch1_Neu
    elif  plane == 'Glu_Neu':
        return Glu_Neu
    elif  plane == 'Sq_Neu':
        return Sq_Neu
    elif plane == 'Neu2_Neu':
        return Neu2_Neu


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
  


def Select_Missing_Tx( Slep, Neu, Neu2, Ch1, Glu, Sq, Weight, TxName='', TxList = ''):
    SLEP, GLU, NEU, SQ, CH1, NEU2, W = [],[],[],[],[],[],[]
    for num in range(len(Neu)):
        if TxList[num] == TxName:
           SLEP.append(Slep[num])
           GLU .append(Glu[num])
           NEU .append(abs(Neu[num]))
           SQ  .append(Sq[num])
           CH1 .append(Ch1[num])
           NEU2.append(abs(Neu2[num]))
           W  .append(Weight[num])
    return SLEP, GLU, NEU, NEU2, SQ, CH1, W

TxNames = ['TChiChipm_Woff_', 'TChiChipmZoff_Woff_','TSnuSnu__','TChiChipm_W_', 'TChiChi__','TChiChipme__']

Planes = ['Slep_Neu', 'Ch1_Neu', 'Glu_Neu', 'Sq_Neu', 'Neu2_Neu']

Marker_Size = 10
BINS = 5
FONTSIZE = 20
REV = False
VMAX = 5


""" Weights of each best Missing Topology """

for T in TxNames:
    Slep, Glu, Neu, Neu2, Sq,Ch1, W = Select_Missing_Tx( SLEP, NEU, NEU2, CH1, GLU, SQ, MISS_TOPO_W, TxName = T , TxList = MISS_TOPO_TX ,)
    if len(Neu) ==0: 
        print ' The TxName ', T , ' has no points satisfying the selection requirements!'
        continue 
    for P in Planes:    
    #plt.scatter(-100,-100, color = 'gray', label = r'Only rValue > 0.9: ' + str(len(X)) )
    #plt.scatter(-100,-100, color = 'gray', label = r'Only rValue > 0.9: ' + str(len(X)) )                                                                                                  
    #plt.scatter(X, Y, c =  Z , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none' , vmin=1, vmax = 5 )
    
        NEU, NEU2, GLU, SQ, CH1, SLEP = Neu, Neu2, Glu, Sq, Ch1, Slep
        Dic_Prop = Plane_Prop(P)
        Plot_Properties(Dic_Prop)

        sel_values = str(min_r) + r' $\leq $' + 'rValue' + r'$<$ ' + str(max_r)+ '\n' + 'ScyNet ' + r'$\chi ^2 \geq$ ' + str(min_Chi2)
 
        plt.text(Dic_Prop['x_lab_pos'], Dic_Prop['y_lab_pos'], sel_values, fontsize = FONTSIZE-6, color = 'blue' )

        leg_lab = 'TxName: '+ T + '\n' + 'Points: ' + str(len(NEU))
        plt.scatter(-100,-100, color = 'gray', label = leg_lab )                                                                                        

        #print Dic_Prop['X'], Dic_Prop['Y'], W
        plt.scatter(Dic_Prop['X'], Dic_Prop['Y'], c =W , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none' , vmin=1, vmax = 5 )
        Color_Bar(plt , size = FONTSIZE , bins = BINS , title = Weight )

        plt.legend(loc ='upper right', fontsize = FONTSIZE-9, fancybox = True)
        plt.savefig('Plots/Missing_Weights/'+ pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')                                                                                              
        plt.savefig('/afs/hephy.at/user/f/fambrogi/www/Fittino/Missing_Weights/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')           
        plt.close()


'''
Colors = ['blue','yellow','lime','red','gray','magenta']

for T,C in zip(TxNames,Colors):                                                                                                                                               
    Slep, Glu, Neu, Sq,Ch1 = Select_Missing_Tx(T , MISS_TOPO_TX, SLEP, NEU, CH1, GLU, SQ)   
    plt.scatter(Slep,Neu, label = T, color = C, s = 8)
    plt.legend(fontsize = 8, loc = 'upper right')
    plt.title('Missing Topologies with TxNames')
    plt.axis([0, 700, 0, 400])
    plt.xlabel(Slep_M, fontsize = FONTSIZE)
    plt.ylabel(Neu_M , fontsize = FONTSIZE)
plt.savefig('Plots/'+ pref + '_Missing.pdf', bbox_inches='tight')
plt.savefig('/afs/hephy.at/user/f/fambrogi/www/Fittino/'+ pref + '_Missing.pdf', bbox_inches='tight' ) 
plt.close()



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

 
