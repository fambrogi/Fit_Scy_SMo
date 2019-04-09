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
max_r = 100
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
MISS_TOPO_W , MISS_TOPO_TX ,CHI2 = dic['MissTopoW'] , dic['MissTopoTx'] , dic['Chi2']

DIFFN2N1 = []
for n1,n2 in zip (NEU, NEU2):
    DIFFN2N1.append(n2-n1)
 
 
# PLOTTING SECTION




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
                           'xmin': 0 ,'xmax':700 ,
                           'ymin': 0 ,'ymax': Max_Neu ,
                           'x_lab_pos': 30 , 'y_lab_pos': 350 ,
                           'xlab': Ch1_M , 'ylab': Neu_M } , 
   
               'Glu_Neu' : { 'X':'GLU' , 'Y': 'NEU',
                           'xmin': 2300 ,'xmax':3500 ,
                           'ymin': 0 ,'ymax': Max_Neu ,
                           'x_lab_pos': 2350 , 'y_lab_pos': 350 ,
                           'xlab': Glu_M , 'ylab': Neu_M } ,

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
               
               'DiffN2N1_Neu' : {'X': 'NEU', 'Y': 'DIFFN2N1' ,
                            'xmin': 0 ,'xmax': 700 ,
                            'ymin': 0 ,'ymax': 600 ,
                            'x_lab_pos': 30, 'y_lab_pos': 650 ,
                            'xlab': Neu_M , 'ylab': DiffN2N1_M  }
               
               }
               
               }
               
               
               
def Color_Bar(plt , size = '' , bins = '' , title = '' , vmin = '', vmax = ''):
    cbar = plt.colorbar(bins = bins, ticks=range(10),  vmin=vmin, vmax = vmx ) 
    cbar.set_label( title , rotation = 90, fontsize = size)
    tick_locator = ticker.MaxNLocator(nbins=bins)
    cbar.locator = tick_locator
    cbar.update_ticks()

def Plot_Properties(Dic_Prop):
    plt.xlabel(Dic_Prop['xlab'],fontsize  =FONTSIZE)                     
    plt.ylabel(Dic_Prop['ylab'] , fontsize = FONTSIZE) 
    plt.grid(color = 'lightgray' , linestyle = ':')
    plt.axis([ Dic_Prop['xmin'], Dic_Prop['xmax'], Dic_Prop['ymin'] , Dic_Prop['ymax'] ])  
  


def Select_Missing_Tx( Slep, Neu, Neu2, Ch1, Glu, Sq, DiffN2N1, Weight, , Chi2, TxName='', TxList = ''):
    ''' Extracts the values of masses and rvalues/chi2 for the selected txName 
        txName is the wanted txname or constraint 
        Txlist is the array of best misisng txnames
    '''
    SLEP, GLU, NEU, SQ, CH1, NEU2,  DIFFN2N1 , W , CHI2 = [],[],[],[],[],[],[], [] , []
    for num in range(len(Neu)):
        if TxList[num] == TxName:
            SLEP.append(Slep[num])
            GLU .append(Glu[num])
            NEU .append(abs(Neu[num]))
            SQ  .append(Sq[num])
            CH1 .append(Ch1[num])
            NEU2.append(abs(Neu2[num]))
            DIFFN2N1.append(DiffN2N1[num])
            W  .append(Weight[num])
            CHI2.append(Chi2[num])
            
    d = dict(SLEP = SLEP, GLU = GLU, NEU=NEU, NEU2=NEU2, SQ=SQ, CH1=CH1, W=W, DIFFN2N1 = DIFFN2N1, CHI2 = CHI2)       
    
    return d 

TxNames = ['TChiChipm_Woff_', 'TChiChipmZoff_Woff_', 'TSnuSnu__', 'TChiChipm_W_', 'TChiChi__','TChiChipme__']


TxNames = ['TChiChipme__' , 'TChiChi__', 'TChiChipm_W_', 'TSnuSnu__', 'TChiChipmZoff_Woff_' , 'TChiChipm_Woff_' ]


Planes = Plane_Prop['planes'].keys()

Marker_Size = 10
BINS = 10
FONTSIZE = 20
REV = False
VMAX = 10
vmin = 0

#MissCon = ['[[],[[jet,jet]]]', '[[],[[l]]]'] # most interesting missing contraints TGN and TChiSlep

#MissCon = ['[[],[[l]]]']

""" Weights of each best Missing Topology """
os.system('mkdir PLOTS')
os.system('mkdir PLOTS/Missing_Weights')


def sub_histo(chi2,fnt_size):
    plot = plt.hist( chi2, bins = 200, label = r'ScyNet $\chi ^2$' , color = 'blue' , fontsize = fnt_size)
    plt.xaxis(0,120)
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
        
        plt.figure(figsize=(8,4))
        Plot_Properties ( Plane_Prop['planes'][P] ) 

        sel_values = str(min_r) + r' $\leq $' + 'rValue' + r'$<$ ' + str(max_r)+ '\n' + 'ScyNet ' + r'$\chi ^2 \geq$ ' + str(min_Chi2)
 
        plt.text(Plane_Prop['planes'][P]['x_lab_pos'], Plane_Prop['planes'][P]['y_lab_pos'], sel_values, fontsize = FONTSIZE-6, color = 'blue' )

        plt.title('TxName: '+ T.replace('_','').replace('__','') , fontsize = fnt_size , color = 'dodgerblue' )
        #plt.scatter(-100,-100, color = 'gray', label = leg_lab )                                                                                        

        #print Dic_Prop['X'], Dic_Prop['Y'], W
        plt.scatter( res[Plane_Prop['planes'][P]['X']],   res[Plane_Prop['planes'][P]['Y']],  c = res['W'] , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none', vmin = vmin, vmax = VMAX )

        Color_Bar(plt , size = FONTSIZE , bins = BINS , title = Weight , vmin = vmin, vmax = VMAX  )
        cbar = plt.colorbar(bins = bins, ticks=range(10),  vmin=vmin, vmax = vmx ) 
        plt.legend(loc ='upper right', fontsize = FONTSIZE-9, fancybox = True)

        os.system('mkdir Plots/Missing_Weights/' + T )
        plt.savefig('Plots/Missing_Weights/'+ T + '/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')
        #plt.savefig('/afs/hephy.at/user/f/fambrogi/www/Fittino/Missing_Weights_TxName/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')           
        plt.close()

'''

'''
pref = 'minRvalue_'+ str(min_r) + '_MAXrValue_' + str(max_r) +'_minXi2_' + str(min_Chi2)

'''
### Looping over the missing contraints
for tt in MissCon:
    T = tt
    Slep, Glu, Neu, Neu2, Sq,Ch1, W = Select_Missing_Tx( SLEP, NEU, NEU2, CH1, GLU, SQ, MISS_TOPO_W, TxName = T , TxList = MISS_CON_BRA ,)
    if len(Neu) ==0:
        print (' *** The Missing Constraint ', T , ' has no points satisfying the selection requirements!')
        continue
    else:  print ('*** The Missing Constraint ' , T, '  will be analysed ! ****')
    for P in Planes:
        NEU, NEU2, GLU, SQ, CH1, SLEP = Neu, Neu2, Glu, Sq, Ch1, Slep
        Dic_Prop = Plane_Prop(P)
        Plot_Properties(Dic_Prop)

        sel_values = str(min_r) + r' $\leq $' + 'rValue' + r'$<$ ' + str(max_r)+ '\n' + 'ScyNet ' + r'$\chi ^2 \geq$ ' + str(min_Chi2)

        plt.text(Dic_Prop['x_lab_pos'], Dic_Prop['y_lab_pos'], sel_values, fontsize = FONTSIZE-6, color = 'blue' )

        leg_lab = 'TxName: '+ T + '\n' + 'Points: ' + str(len(NEU))
        plt.scatter(-100,-100, color = 'gray', label = leg_lab )

        #print Dic_Prop['X'], Dic_Prop['Y'], W
        print('W is', W)
        plt.scatter(Dic_Prop['X'], Dic_Prop['Y'], c =W , marker = 'o', s = Marker_Size ,  cmap = cm.jet,edgecolors='none' , vmin=1, vmax = 5 )
        Color_Bar(plt , size = FONTSIZE , bins = BINS , title = Weight )

        plt.legend(loc ='upper right', fontsize = FONTSIZE-9, fancybox = True)
        T = T.replace(',','')
        os.system('mkdir PLOTS/Missing_Weights/' + T )
        plt.savefig('PLOTS/Missing_Weights/'+ T + '/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')                                                      

        #plt.savefig('/afs/hephy.at/user/f/fambrogi/www/Fittino/Missing_Weights_Constraints/' + pref + '_' + P + '_Weight_'+ T +'.pdf', bbox_inches='tight')
        plt.close()



'''
