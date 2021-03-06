""" 
BUG: must be run twice with the misisng TxNames first then the missing constraints separately
otherwise it says the list is empty

????

"""
import os,sys
import matplotlib
matplotlib.use('Agg')
from matplotlib  import cm
from matplotlib import ticker
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import argparse
import numpy as np
from Extract_Info_Plotting import *
#
#
#
#Extracting Results

min_r = 0
max_r = 1
min_Chi2 = 0


''' Content of the dictionary from the function below ::: 
dic = {'Neu'         : NEU  , 
       'Neu2'        : NEU2 , 
       'Slep'        : SLEP , 
       'Chi1'        : CH1  , 
       'rValue'      : R    , 
       'chi2'        : XI2  ,
       'MissTopoBra' : MISS_TOPO_BRA ,
       'MissTopoTx'  : MISS_TOPO_TX  ,
       'MissTopoW'   : MISS_TOPO_W   ,
       'MissConBra'  : MISS_CON_BRA  ,
       'MissConW'    : MISS_CON_W }
'''

''' Selecting the results '''
dic = Select_Results(min_r = min_r , max_r = max_r, min_xi= min_Chi2, max_xi= 10000)

SLEP , NEU, CH1 , NEU2 , SQ, GLU = dic['Slep'] , dic['Neu'] , dic['Ch1'] , dic['Neu2'] , dic['Sq'] , dic['Glu']
MISS_TOPO_W , MISS_TOPO_TX ,CHI2 = dic['MissTopoW'] , dic['MissTopoTx'] , dic['chi2']

OUTSIDE , OUTSIDE_W = dic['OutGrid'] , dic['OutGridW']

DIFFN2N1 = []
DIFFGN1= []

for n1,n2,g in zip (NEU, NEU2,GLU):
    DIFFN2N1.append(n2-n1)
    DIFFGN1.append(g-n1)

# PLOTTING SECTION


print(len(NEU), len(NEU2), len(GLU))

fnt_size = 13
histtype = 'stepfilled'
fill = True
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''   RVALUES and CHI2 DISTRIBUTIONS
plt.hist(dic['rValue'], bins = 250 , histtype = histtype, fill = fill,  color = 'slateblue'  , label = 'SModelS rvalue'  )
plt.legend(loc = 'upper right' , fontsize = fnt_size -2 , ncol = 2)
plt.xlabel('rvalue', fontsize = fnt_size)
plt.axis([0,5,0,5000])
plt.grid(color = 'lightgray', linestyle = ':')
os.system('mkdir PLOTS/rvalues_chi2')
plt.savefig('PLOTS/rvalues_chi2/rvalues.png' , bbox_inches='tight' , dpi = 200)
plt.close()
# ****
plt.hist(dic['chi2'], bins = 200 , histtype = histtype, fill = fill,  color = 'orange'  , label = 'ScyNet 8TeV $\chi ^2$'  )
plt.legend(loc = 'upper right' , fontsize = fnt_size -2 , ncol = 2)
plt.grid(color = 'lightgray', linestyle = ':')
plt.xlabel('ScyNet 8TeV $\chi ^2$' , fontsize = fnt_size)
plt.axis([20,120,0,2000])

os.system('mkdir PLOTS/rvalues_chi2')
plt.savefig('PLOTS/rvalues_chi2/chi2.png' , bbox_inches='tight' , dpi = 200)
plt.close()



# To do: distributions of points with r>1 and chi large -> need also info on the analysis used by smodels!




# This must be improved
Max_Neu = 400




Plane_Prop = {  'Max_Neu' : Max_Neu , 'planes': {
                'Slep_Neu' : { 'X': 'SLEP', 'Y': 'NEU', 
                              'xmin': 0 , 'xmax': 800 ,
                              'ymin': 0 , 'ymax': Max_Neu ,
                              'x_lab_pos': 30 , 'y_lab_pos': 350 ,
                              'xlab': Slep_M , 'ylab': Neu_M } ,
   
               'Ch1_Neu' : { 'X':'CH1' , 'Y': 'NEU',
                           'xmin': 50 ,'xmax':400 ,
                           'ymin': 50 ,'ymax': Max_Neu ,
                           'x_lab_pos': 70 , 'y_lab_pos': 360 ,
                           'xlab': Ch1_M , 'ylab': Neu_M } , 
   
               'Glu_Neu' : { 'X':'GLU' , 'Y': 'NEU',
                           'xmin': 2300 ,'xmax':3500 ,
                           'ymin': 0 ,'ymax': Max_Neu ,
                           'x_lab_pos': 2350 , 'y_lab_pos': 350 ,
                           'xlab': Glu_M , 'ylab': Neu_M } ,

               'Glu_Sq' : { 'X':'GLU' , 'Y': 'SQ',
                           'xmin': 2300 ,'xmax':3500 ,
                           'ymin': 2300 ,'ymax': 3500 ,
                           'x_lab_pos': 2350 , 'y_lab_pos': 3300 ,
                           'xlab': Glu_M , 'ylab': Sq_M } ,
               
               'Sq_Neu' : { 'X': 'SQ', 'Y': 'NEU' ,
                          'xmin': 2300 ,'xmax':3500 ,
                          'ymin': 0 ,'ymax': Max_Neu ,
                          'x_lab_pos': 2350 , 'y_lab_pos': 350 ,
                          'xlab': Sq_M , 'ylab': Neu_M  } ,
               
               'Neu2_Neu' : { 'X': 'NEU2', 'Y': 'NEU' ,
                            'xmin': 0 ,'xmax': 700 ,
                            'ymin': 0 ,'ymax': Max_Neu ,
                            'x_lab_pos': 30, 'y_lab_pos': 340 ,
                            'xlab': Neu2_M , 'ylab': Neu_M  } ,
               
               'DiffN2N1_Neu' : {'X': 'NEU2', 'Y': 'DIFFN2N1' ,
                            'xmin': 0 ,'xmax': 700 ,
                            'ymin': 0 ,'ymax': 600 ,
                            'x_lab_pos': 30, 'y_lab_pos': 530 ,
                            'xlab': Neu2_M , 'ylab': DiffN2N1_M  } ,

               'DiffN2N1_Neu_Zoom' : {'X': 'NEU', 'Y': 'DIFFN2N1' ,
                            'xmin': 0 ,'xmax': 700 ,
                            'ymin': 0 ,'ymax': 50 ,
                            'x_lab_pos': 30, 'y_lab_pos': 43 ,
                            'xlab': Neu_M , 'ylab': DiffN2N1_M  } ,

               'DiffGN1_Neu_Zoom' : {'X': 'GLU', 'Y': 'DIFFGN1' ,
                            'xmin': 0 ,'xmax': 700 ,
                            'ymin': 0 ,'ymax': 50 ,
                            'x_lab_pos': 30, 'y_lab_pos': 43 ,
                            'xlab': Glu_M , 'ylab': DiffGN1_M  } ,

               
               }
               
               }
               
               
               
def Color_Bar(plt , size = '' , bins = '' , title = '' , vmin = '', vmax = ''):
    cbar = plt.colorbar() 
    cbar.set_label( title , rotation = 90, fontsize = size)
    tick_locator = ticker.MaxNLocator(nbins=bins)
    cbar.locator = tick_locator
    cbar.update_ticks()

def Plot_Properties(Dic_Prop):
    plt.xlabel(Dic_Prop['xlab'] , fontsize = FONTSIZE+2)                                                                                                                      
    plt.ylabel(Dic_Prop['ylab'] , fontsize = FONTSIZE+2) 
    plt.grid(color = 'lightgray' , linestyle = ':')
    plt.axis([ Dic_Prop['xmin'], Dic_Prop['xmax'], Dic_Prop['ymin'] , Dic_Prop['ymax'] ])  
  


def Select_Missing_Tx( Slep, Neu, Neu2, Ch1, Glu, Sq, DiffN2N1, DiffGN1, Weight, Chi2, TxName='', TxList = ''):
    ''' Extracts the values of masses and rvalues/chi2 for the selected txName 
        txName is the wanted txname or constraint 
        Txlist is the array of best misisng txnames
    '''
    SLEP, GLU, NEU, SQ, CH1, NEU2,  DIFFN2N1 ,DIFFGN1, W , CHI2 = [],[],[],[],[],[],[], [] , [], []
    for num in range(len(Neu)):
        if TxList[num] == TxName:
            SLEP.append(Slep[num])
            GLU .append(Glu[num])
            NEU .append(abs(Neu[num]))
            SQ  .append(Sq[num])
            CH1 .append(Ch1[num])
            NEU2.append(abs(Neu2[num]))
            DIFFN2N1.append(DiffN2N1[num])
            DIFFGN1.append(DiffGN1[num])
            W  .append(Weight[num])
            CHI2.append(Chi2[num])
            
    d = dict(SLEP = SLEP, GLU = GLU, NEU=NEU, NEU2=NEU2, SQ=SQ, CH1=CH1, W=W, DIFFN2N1 = DIFFN2N1, CHI2 = CHI2 , DIFFGN1 = DIFFGN1)       
    
    return d 



'''
TxNames = ['TChiChipm_Woff_', 'TChiChipmZoff_Woff_','TSnuSnu__','TChiChipm_W_', 'TChiChi__','TChiChipme__']

Planes = Plane_Prop['planes'].keys()

Marker_Size = 10
BINS = 10
FONTSIZE = 20
REV = False
vmin = 0
VMAX = 10


#MissCon = ['[[],[[jet,jet]]]', '[[],[[l]]]'] # most interesting missing contraints TGN and TChiSlep


""" Weights of each best Missing Topology """
os.system('mkdir PLOTS')
os.system('mkdir PLOTS/Missing_Weights')


def sub_histo(chi2,fnt_size):
    plot = plt.hist( chi2, bins = 40, label = r'ScyNet $\chi ^2$' , color = 'slateblue')
    plt.legend(fontsize = fnt_size, loc = 'upper left')
    plt.axis( ( 0,120, 0, 200) )
    plt.grid(color = 'lightgray' , linestyle = ':' )
    return plot    
    
    

pref = 'prova'
for T in TxNames:
    # Slep, Neu, Neu2, Ch1, Glu, Sq, DiffN2N1, Weight, TxName='', TxList = ''
    res = Select_Missing_Tx( SLEP, NEU, NEU2, CH1, GLU, SQ, DIFFN2N1, MISS_TOPO_W, CHI2, TxName = T , TxList = MISS_TOPO_TX ,)
    
    if len(res['NEU']) ==0: 
        print (' The TxName ', T , ' has no points satisfying the selection requirements!')
        continue 
    
    else: print ('The TxName ', T , ' will be analysed ! ****')
    for P in Planes:       
                
        plt.figure(figsize=(9,7))
        ax1 = plt.axes([0.1 , 0.1, 0.95, 0.95])
        ax2 = plt.axes([0.58 , 0.80, 0.26, 0.22])
        
        plt.axes(ax1)
        Plot_Properties ( Plane_Prop['planes'][P] ) 

        sel_values = str(min_r) + r' $\leq $' + 'rValue' + r'$<$ ' + str(max_r)+ '\n' + 'ScyNet ' + r'$\chi ^2 \geq$ ' + str(min_Chi2)
 
        plt.text(Plane_Prop['planes'][P]['x_lab_pos'], Plane_Prop['planes'][P]['y_lab_pos'], sel_values, fontsize = FONTSIZE-2, color = 'blue' )

        plt.title('TxName: '+ T.replace('_','').replace('__','') , fontsize = fnt_size+3 , color = 'dodgerblue' , y = 1.03 )
        #plt.scatter(-100,-100, color = 'gray', label = leg_lab )                                                   
        ax1.tick_params(axis = 'both', which = 'major', labelsize = fnt_size-1)
                           
        #print Dic_Prop['X'], Dic_Prop['Y'], W
        plt.scatter( res[Plane_Prop['planes'][P]['X']],   res[Plane_Prop['planes'][P]['Y']],  c = res['W'] , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none' , vmin=vmin, vmax = VMAX )
        Color_Bar(plt , size = FONTSIZE  , title = Weight , bins = BINS )
        plt.legend(loc ='upper right', fontsize = FONTSIZE-9, fancybox = True)

        plt.axes(ax2)
        sub_histo(res['CHI2'], fnt_size-2)
        ax2.tick_params(axis = 'both', which = 'major', labelsize = fnt_size-1)
 
        os.system('mkdir Plots/Missing_Weights/' + T )
        plt.savefig('Plots/Missing_Weights/'+ T + '/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')
        #plt.savefig('/afs/hephy.at/user/f/fambrogi/www/Fittino/Missing_Weights_TxName/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')           
        plt.close()
'''




Out = OUTSIDE
for i in list(set(Out)):
    print(' i, frequency', i , Out.count(i))
    
O = ['[[[jet]],[[jet]]]','[[[jet,jet]],[[jet,jet]]]' , '[[[l],[l]],[[l],[nu]]]' ]

Planes = Plane_Prop['planes'].keys()

Marker_Size = 10
BINS = 10
FONTSIZE = 20
REV = False
vmin = 0
VMAX = 10


#MissCon = ['[[],[[jet,jet]]]', '[[],[[l]]]'] # most interesting missing contraints TGN and TChiSlep


""" Weights of each best Missing Topology """
os.system('mkdir PLOTS')
os.system('mkdir PLOTS/Missing_Weights')


def sub_histo(chi2,fnt_size):
    plot = plt.hist( chi2, bins = 40, label = r'ScyNet $\chi ^2$' , color = 'slateblue')
    plt.legend(fontsize = fnt_size, loc = 'upper left')
    plt.axis( ( 0,120, 0, 200) )
    plt.grid(color = 'lightgray' , linestyle = ':' )
    return plot    
    
    

pref = 'prova'
for T in O:
    # Slep, Neu, Neu2, Ch1, Glu, Sq, DiffN2N1, Weight, TxName='', TxList = ''
    res = Select_Missing_Tx( SLEP, NEU, NEU2, CH1, GLU, SQ, DIFFN2N1, DIFFGN1, MISS_TOPO_W, CHI2, TxName = T , TxList = Out ,)
    
    if len(res['NEU']) ==0: 
        print (' The TxName ', T , ' has no points satisfying the selection requirements!')
        continue 
    
    else: print ('The TxName ', T , ' will be analysed ! ****')
    for P in Planes:       
                
        plt.figure(figsize=(9,7))
        ax1 = plt.axes([0.1 , 0.1, 0.95, 0.95])
        ax2 = plt.axes([0.58 , 0.80, 0.26, 0.22])
        
        plt.axes(ax1)
        Plot_Properties ( Plane_Prop['planes'][P] ) 

        sel_values = str(min_r) + r' $\leq $' + 'rValue' + r'$<$ ' + str(max_r)+ '\n' + 'ScyNet ' + r'$\chi ^2 \geq$ ' + str(min_Chi2)
        print('P is: ', P)
        plt.text(Plane_Prop['planes'][P]['x_lab_pos'], Plane_Prop['planes'][P]['y_lab_pos'], sel_values, fontsize = FONTSIZE-2, color = 'blue' )

        plt.title('TxName: '+ T.replace('_','').replace('__','') , fontsize = fnt_size+3 , color = 'dodgerblue' , y = 1.03 )
        #plt.scatter(-100,-100, color = 'gray', label = leg_lab )                                                   
        ax1.tick_params(axis = 'both', which = 'major', labelsize = fnt_size-1)
                           
        #print Dic_Prop['X'], Dic_Prop['Y'], W
        plt.scatter( res[Plane_Prop['planes'][P]['X']],   res[Plane_Prop['planes'][P]['Y']],  c = res['W'] , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none' , vmin=vmin, vmax = VMAX )
        Color_Bar(plt , size = FONTSIZE  , title = Weight , bins = BINS )
        plt.legend(loc ='upper right', fontsize = FONTSIZE-9, fancybox = True)

        plt.axes(ax2)
        sub_histo(res['CHI2'], fnt_size-2)
        ax2.tick_params(axis = 'both', which = 'major', labelsize = fnt_size-1)
        T = T.replace(',','') 
        os.system('mkdir Plots/Outside_Weights/' )        
        os.system('mkdir Plots/Outside_Weights/' + T)
        plt.savefig('Plots/Outside_Weights/'+ T + '/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')
        #plt.savefig('/afs/hephy.at/user/f/fambrogi/www/Fittino/Missing_Weights_TxName/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')           
        plt.close()
        
        
        