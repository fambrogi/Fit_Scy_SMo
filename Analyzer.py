"""
    Module::  Analyzer.py
    Author::  Federico Ambrogi, federico.ambrogi88@gmail.com
    Summary:: This script analyses the root file produced by Fittino
"""

import os,sys
import ROOT as ROOT 
import numpy as np

Input = 'Trees/Fittino_431_part.root'  ### Select the input file

""" Loading the input file """

c = ROOT.TChain('Tree')
c.Add("Trees/Fittino_431_part.root")

File = ROOT.TFile(Input)
Tree = File.Get('Tree')

Num_Points = Tree.GetEntries()
Branches = Tree.GetListOfBranches()
print '*** List of available branches : *** '
for B in Branches:
    print B

'''
Chi2_8TeV_Scy = Tree.GetBranch('SCYNet_Chi2_8TeV')
rValue        = Tree.GetBranch('SModelSCalculator_RValue')
Smo_Status    = Tree.GetBranch('SModelSCalculator_DecompositionStatus')

""" Masses of SUSY particles.
    Note that since it is pMSSM-11 , all the light squarks are degenerate , as well as 1st and 2nd gen leptons """
Glu    = Tree.GetBranch('SPheno_Mass_~g')
Neu    = Tree.GetBranch('SPheno_Mass_~chi10')
'''


Num_Points = c.GetEntries()
print 'Total number of points: ', Num_Points


Dic = { 'Glu': []  , 'Neu1': [] , 'Neu2': [] , 'Ch1': [] , 'Slep': []  , 'Sq': []  , 'Ch2':[] ,
        'ScyChi2': [] , 'rValue': [] , 
        'Miss_Topo_Tx': [] , 'Miss_Topo_Bra':[], 'Miss_Con_Bra':[] , 
        'Miss_Topo_W':[], 'Miss_Con_W':[] }


for P in range(Num_Points):
    #print '*** Checking: ' , P

    c.GetEntry(P) 
    glu    = c.GetLeaf("SPheno_Mass_~g").GetValue()
    Neu1   = abs( c.GetLeaf("SPheno_Mass_~chi10").GetValue() )
    Neu2   = abs( c.GetLeaf('SPheno_Mass_~chi20').GetValue() )
    Neu3   = abs( c.GetLeaf('SPheno_Mass_~chi30').GetValue() )
    Neu4   = abs( c.GetLeaf('SPheno_Mass_~chi40').GetValue() )
    Ch1    = abs( c.GetLeaf('SPheno_Mass_~chi1p').GetValue() )
    Ch2    = abs( c.GetLeaf('SPheno_Mass_~chi2p').GetValue() )   

    EL     = c.GetLeaf('SPheno_Mass_~eL').GetValue()
    ER     = c.GetLeaf('SPheno_Mass_~eR').GetValue()
    MuL    = c.GetLeaf('SPheno_Mass_~muL').GetValue()
    MuR    = c.GetLeaf('SPheno_Mass_~muR').GetValue()

    Sq     = c.GetLeaf('SPheno_Mass_~dL').GetValue() 

    # SMo rvalues and ScyNet chi2

    rValue   = c.GetLeaf('SModelS_Measurement_Rvalue').GetValue()
    rValue_2 = c.GetLeaf('SModelSCalculator_RValue').GetValue()
    ScyChi2 = c.GetLeaf('SCYNet_Chi2_8TeV').GetValue()


    #SModelSCalculator_MissingConstraint_0_Weight = c.SModelSCalculator_MissingConstraint_0_Weight
    #SModelSCalculator_UnusedModel_0_Bracket      = c.SModelSCalculator_UnusedModel_0_Bracket
    #SModelSCalculator_UnusedModel_0_TxName       = c.SModelSCalculator_UnusedModel_0_TxName
    #MissingConstraint_0_Bracket                  = c.SModelSCalculator_MissingConstraint_0_Bracket

    # Missing topo with proper TxName + brackets + weight
    Miss_Topo_Tx  = str(c.SModelSCalculator_UnusedModel_0_TxName)
    Miss_Topo_Bra = str(c.SModelSCalculator_UnusedModel_0_Bracket)
    Miss_Topo_W   = c.GetLeaf('SModelSCalculator_MissingConstraint_0_Weight').GetValue()

    # Miss topo without TxName
    Miss_Con_Bra  = str(c.SModelSCalculator_MissingConstraint_0_Bracket)  # Miss constraints, i.e. no TxName defined for this topology
    Miss_Con_W    = c.GetLeaf('SModelSCalculator_UnusedModel_0_Bracket').GetValue()


    '''
    print glu, Neu1, Neu2 , EL 
    print 'rvalue1, rvalue2', rValue , rValue_2 
    print 'SModelSCalculator_MissingConstraint_0_Weight' , SModelSCalculator_MissingConstraint_0_Weight 
    print 'SModelSCalculator_MissingConstraint_1_Weight' , SModelSCalculator_MissingConstraint_1_Weight

    print 'SModelSCalculator_UnusedModel_0_Bracket'      , SModelSCalculator_UnusedModel_0_Bracket 
    print 'SModelSCalculator_UnusedModel_0_TxName'       , SModelSCalculator_UnusedModel_0_TxName 
    print 'MissingConstraint_0_Bracket'                  , MissingConstraint_0_Bracket
    '''

   
    Dic['Glu']      .append(glu)
    Dic['Neu1']     .append(Neu1)
    Dic['Neu2']     .append(Neu2)
    Dic['Ch1']      .append(Ch1)
    Dic['Ch2']      . append(Ch2)
    Dic['Slep']     .append(EL)
    Dic['Sq']       .append(Sq)

#         'Miss_Topo_Tx': [] , 'Miss_Topo_Bra':[], 'Miss_Con_Bra':[] , }

    Dic['Miss_Topo_W']  .append(Miss_Topo_W)
    Dic['Miss_Con_W']   .append(Miss_Con_W)
    Dic['rValue']       .append(rValue_2)
    Dic['ScyChi2']      .append(ScyChi2)
    Dic['Miss_Topo_Tx'] .append(Miss_Topo_Tx)
    Dic['Miss_Topo_Bra'].append(Miss_Topo_Bra)
    Dic['Miss_Con_Bra'] .append(Miss_Con_Bra)

np.save('ScyNet_Res', Dic)





