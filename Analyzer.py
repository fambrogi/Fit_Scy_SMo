"""
    Module::  Analyzer.py
    Author::  Federico Ambrogi, federico.ambrogi@univie.ac.at
    Summary:: This script analyses the root file produced by Fittino-ScyNet
              and converts it into a numpy dictionary.

              At the bottom, the list of branches in the root file can be consulted.
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






'''
*** List of available branches : ***
<ROOT.TBranch object ("Minput") at 0x1df4fb0>
<ROOT.TBranch object ("M1") at 0x1e02ca0>
<ROOT.TBranch object ("M2") at 0x1e03800>
<ROOT.TBranch object ("M3") at 0x1e04360>
<ROOT.TBranch object ("MQ1") at 0x1e04ec0>
<ROOT.TBranch object ("MQ3") at 0x1e05a20>
<ROOT.TBranch object ("ML1") at 0x1e06580>
<ROOT.TBranch object ("ML3") at 0x1e070e0>
<ROOT.TBranch object ("MA0") at 0x1e07c40>
<ROOT.TBranch object ("A") at 0x1e087a0>
<ROOT.TBranch object ("Mu") at 0x1e09300>
<ROOT.TBranch object ("TanBeta") at 0x1e09e60>
<ROOT.TBranch object ("Mt") at 0x1e0a9c0>
<ROOT.TBranch object ("Bound_M3") at 0x1e0b520>
<ROOT.TBranch object ("Bound_Mu") at 0x1e0c080>
<ROOT.TBranch object ("SPheno_Mass_Wp") at 0x1e0cbe0>
<ROOT.TBranch object ("SPheno_Mass_Z0") at 0x1e0d740>
<ROOT.TBranch object ("SPheno_Mass_t") at 0x1e0e2d0>
<ROOT.TBranch object ("SPheno_GammaTotal_t") at 0x1e0ee50>
<ROOT.TBranch object ("SPheno_BR_t_to_b_Wp") at 0x1e0fa40>
<ROOT.TBranch object ("SPheno_BR_t_to_b_Hp") at 0x1e10630>
<ROOT.TBranch object ("SPheno_Mass_h0") at 0x1e11220>
<ROOT.TBranch object ("SPheno_GammaTotal_h0") at 0x1e11db0>
<ROOT.TBranch object ("SPheno_Mass_H0") at 0x1e129a0>
<ROOT.TBranch object ("SPheno_GammaTotal_H0") at 0x1e13530>
<ROOT.TBranch object ("SPheno_Mass_Hp") at 0x1e14120>
<ROOT.TBranch object ("SPheno_GammaTotal_Hp") at 0x1e14cb0>
<ROOT.TBranch object ("SPheno_Mass_A0") at 0x1e158a0>
<ROOT.TBranch object ("SPheno_GammaTotal_A0") at 0x1e16430>
<ROOT.TBranch object ("SPheno_HMIX_Q") at 0x1e17020>
<ROOT.TBranch object ("SPheno_HMIX_mu") at 0x1e17ba0>
<ROOT.TBranch object ("SPheno_HMIX_VEV") at 0x1e18730>
<ROOT.TBranch object ("SPheno_BR_b_s_gamma") at 0x1e19300>
<ROOT.TBranch object ("SPheno_BR_Bs_mu_mu") at 0x1e19ef0>
<ROOT.TBranch object ("SPheno_BR_Bu_tau_nu") at 0x1e1aae0>
<ROOT.TBranch object ("SPheno_NormSM_BR_Bu_tau_nu") at 0x1e1b6d0>
<ROOT.TBranch object ("SPheno_Abs_Delta_Mass_Bd") at 0x1e1c2c0>
<ROOT.TBranch object ("SPheno_Abs_Delta_Mass_Bs") at 0x1e1ceb0>
<ROOT.TBranch object ("SPheno_DiffSM_amu") at 0x1e1daa0>
<ROOT.TBranch object ("SPheno_Mass_~dL") at 0x1e1e690>
<ROOT.TBranch object ("SPheno_GammaTotal_~dL") at 0x1e1f260>
<ROOT.TBranch object ("SPheno_Mass_~uL") at 0x1e1fe50>
<ROOT.TBranch object ("SPheno_GammaTotal_~uL") at 0x1e20a20>
<ROOT.TBranch object ("SPheno_Mass_~sL") at 0x1e21610>
<ROOT.TBranch object ("SPheno_GammaTotal_~sL") at 0x1e221e0>
<ROOT.TBranch object ("SPheno_Mass_~cL") at 0x1e22dd0>
<ROOT.TBranch object ("SPheno_GammaTotal_~cL") at 0x1e239a0>
<ROOT.TBranch object ("SPheno_Mass_~b1") at 0x1e24590>
<ROOT.TBranch object ("SPheno_GammaTotal_~b1") at 0x1e25160>
<ROOT.TBranch object ("SPheno_Mass_~t1") at 0x1e25d50>
<ROOT.TBranch object ("SPheno_GammaTotal_~t1") at 0x1e26920>
<ROOT.TBranch object ("SPheno_Mass_~eL") at 0x1e27510>
<ROOT.TBranch object ("SPheno_GammaTotal_~eL") at 0x1e280e0>
<ROOT.TBranch object ("SPheno_Mass_~nueL") at 0x1e28cd0>
<ROOT.TBranch object ("SPheno_GammaTotal_~nueL") at 0x1e298c0>
<ROOT.TBranch object ("SPheno_Mass_~muL") at 0x1e2a4b0>
<ROOT.TBranch object ("SPheno_GammaTotal_~muL") at 0x1e2b0a0>
<ROOT.TBranch object ("SPheno_Mass_~numuL") at 0x1e2bc90>
<ROOT.TBranch object ("SPheno_GammaTotal_~numuL") at 0x1e2c880>
<ROOT.TBranch object ("SPheno_Mass_~tau1") at 0x1e2d470>
<ROOT.TBranch object ("SPheno_GammaTotal_~tau1") at 0x1e2e060>
<ROOT.TBranch object ("SPheno_Mass_~nutauL") at 0x1e2ec50>
<ROOT.TBranch object ("SPheno_GammaTotal_~nutauL") at 0x1e2f840>
<ROOT.TBranch object ("SPheno_Mass_~dR") at 0x1e30430>
<ROOT.TBranch object ("SPheno_GammaTotal_~dR") at 0x1e31000>
<ROOT.TBranch object ("SPheno_Mass_~uR") at 0x1e31bf0>
<ROOT.TBranch object ("SPheno_GammaTotal_~uR") at 0x1e327c0>
<ROOT.TBranch object ("SPheno_Mass_~sR") at 0x1e333b0>
<ROOT.TBranch object ("SPheno_GammaTotal_~sR") at 0x1e33f80>
<ROOT.TBranch object ("SPheno_Mass_~cR") at 0x1e34b70>
<ROOT.TBranch object ("SPheno_GammaTotal_~cR") at 0x1e35740>
<ROOT.TBranch object ("SPheno_Mass_~b2") at 0x1e36330>
<ROOT.TBranch object ("SPheno_GammaTotal_~b2") at 0x1e36f00>
<ROOT.TBranch object ("Sject ("SPheno_BR_~g_to_~t2bar_t") at 0x1e66c40>
<ROOT.TBranch object ("SPheno_BR_~g_to_~uLbar_u") at 0x1e67830>
<ROOT.TBranch object ("SPheno_BR_~g_to_~uRbar_u
'''



