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


raw_input('This is the list of branches')
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
        'Sb1': [] , 'St1': [],
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

    b      = c.GetLeaf('SPheno_Mass_~b1').GetValue()
    t      = c.GetLeaf('SPheno_Mass_~t1').GetValue()


    # SMo rvalues and ScyNet chi2

    rValue   = c.GetLeaf('SModelS_Measurement_Rvalue').GetValue()
    rValue_2 = c.GetLeaf('SModelSCalculator_RValue').GetValue()
    ScyChi2 = c.GetLeaf('SCYNet_Chi2_8TeV').GetValue()


    
    # Missing Constraints ************************
    Miss_Con_W    = c.GetLeaf('SModelSCalculator_MissingConstraint_0_Weight').GetValue()
    Miss_Con_W_1  = c.GetLeaf('SModelSCalculator_MissingConstraint_1_Weight').GetValue()
    Miss_Con_W_2  = c.GetLeaf('SModelSCalculator_MissingConstraint_2_Weight').GetValue()
    Miss_Con_Bra  = str(c.SModelSCalculator_MissingConstraint_0_Bracket)

    # Unused Models ***************************
    Unused_Tx  = str(c.SModelSCalculator_UnusedModel_0_TxName)
    Unused_Bra = str(c.SModelSCalculator_UnusedModel_0_Bracket)
    Unused_W     = c.GetLeaf('SModelSCalculator_UnusedModel_0_Weight').GetValue()
    Unused_W_1   = c.GetLeaf('SModelSCalculator_UnusedModel_1_Weight').GetValue()
    Unused_W_2   = c.GetLeaf('SModelSCalculator_UnusedModel_2_Weight').GetValue()

    # Our grid ********************************
    Out_grid    = str(c.SModelSCalculator_ConstraintOutsideGrid_0_Bracket)
    Out_grid_W  = c.GetLeaf('SModelSCalculator_ConstraintOutsideGrid_0_Weight').GetValue()  
      

 #   if ScyChi2 > 80 and rValue < 1:
 #       print('Miss Con: bra, w1, w2, w3',  Miss_Con_Bra, Miss_Con_W, Miss_Con_W_1 , Miss_Con_W_2 #)
 #        print('Unused models tx, brax, w , w1', Unused_Tx , Unused_Bra, Unused_W, Unused_W_1 )
 #        print('Outside grid:', Out_grid , ' ' , Out_grid_W)
 #        raw_input('check!')

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
    Dic['Ch2']      .append(Ch2)
    Dic['Slep']     .append(EL)
    Dic['Sq']       .append(Sq)
    Dic['Sb1']      .append(b)
    Dic['St1']      .append(t)


#         'Miss_Topo_Tx': [] , 'Miss_Topo_Bra':[], 'Miss_Con_Bra':[] , }

    #Dic['Miss_Topo_W']  .append(Miss_Topo_W)
    #Dic['Miss_Con_W']   .append(Miss_Con_W)
    #Dic['Miss_Topo_Tx'] .append(Miss_Topo_Tx)
    #Dic['Miss_Topo_Bra'].append(Miss_Topo_Bra)
    #Dic['Miss_Con_Bra'] .append(Miss_Con_Bra)

    Dic['rValue']       .append(rValue_2)
    Dic['ScyChi2']      .append(ScyChi2)


np.save('ScyNet_Res', Dic)






'''
*** List of available branches : ***

<ROOT.TBranch object ("Minput") at 0x2caf270>
<ROOT.TBranch object ("M1") at 0x2cbcf60>
<ROOT.TBranch object ("M2") at 0x2cbdac0>
<ROOT.TBranch object ("M3") at 0x2cbe620>
<ROOT.TBranch object ("MQ1") at 0x2cbf180>
<ROOT.TBranch object ("MQ3") at 0x2cbfce0>
<ROOT.TBranch object ("ML1") at 0x2cc0840>
<ROOT.TBranch object ("ML3") at 0x2cc13a0>
<ROOT.TBranch object ("MA0") at 0x2cc1f00>
<ROOT.TBranch object ("A") at 0x2cc2a60>
<ROOT.TBranch object ("Mu") at 0x2cc35c0>
<ROOT.TBranch object ("TanBeta") at 0x2cc4120>
<ROOT.TBranch object ("Mt") at 0x2cc4c80>
<ROOT.TBranch object ("Bound_M3") at 0x2cc57e0>
<ROOT.TBranch object ("Bound_Mu") at 0x2cc6340>
<ROOT.TBranch object ("SPheno_Mass_Wp") at 0x2cc6ea0>
<ROOT.TBranch object ("SPheno_Mass_Z0") at 0x2cc7a00>
<ROOT.TBranch object ("SPheno_Mass_t") at 0x2cc8590>
<ROOT.TBranch object ("SPheno_GammaTotal_t") at 0x2cc9110>
<ROOT.TBranch object ("SPheno_BR_t_to_b_Wp") at 0x2cc9d00>
<ROOT.TBranch object ("SPheno_BR_t_to_b_Hp") at 0x2cca8f0>
<ROOT.TBranch object ("SPheno_Mass_h0") at 0x2ccb4e0>
<ROOT.TBranch object ("SPheno_GammaTotal_h0") at 0x2ccc070>
<ROOT.TBranch object ("SPheno_Mass_H0") at 0x2cccc60>
<ROOT.TBranch object ("SPheno_GammaTotal_H0") at 0x2ccd7f0>
<ROOT.TBranch object ("SPheno_Mass_Hp") at 0x2cce3e0>
<ROOT.TBranch object ("SPheno_GammaTotal_Hp") at 0x2ccef70>
<ROOT.TBranch object ("SPheno_Mass_A0") at 0x2ccfb60>
<ROOT.TBranch object ("SPheno_GammaTotal_A0") at 0x2cd06f0>
<ROOT.TBranch object ("SPheno_HMIX_Q") at 0x2cd12e0>
<ROOT.TBranch object ("SPheno_HMIX_mu") at 0x2cd1e60>
<ROOT.TBranch object ("SPheno_HMIX_VEV") at 0x2cd29f0>
<ROOT.TBranch object ("SPheno_BR_b_s_gamma") at 0x2cd35c0>
<ROOT.TBranch object ("SPheno_BR_Bs_mu_mu") at 0x2cd41b0>
<ROOT.TBranch object ("SPheno_BR_Bu_tau_nu") at 0x2cd4da0>
<ROOT.TBranch object ("SPheno_NormSM_BR_Bu_tau_nu") at 0x2cd5990>
<ROOT.TBranch object ("SPheno_Abs_Delta_Mass_Bd") at 0x2cd6580>
<ROOT.TBranch object ("SPheno_Abs_Delta_Mass_Bs") at 0x2cd7170>
<ROOT.TBranch object ("SPheno_DiffSM_amu") at 0x2cd7d60>
<ROOT.TBranch object ("SPheno_Mass_~dL") at 0x2cd8950>
<ROOT.TBranch object ("SPheno_GammaTotal_~dL") at 0x2cd9520>
<ROOT.TBranch object ("SPheno_Mass_~uL") at 0x2cda110>
<ROOT.TBranch object ("SPheno_GammaTotal_~uL") at 0x2cdace0>
<ROOT.TBranch object ("SPheno_Mass_~sL") at 0x2cdb8d0>
<ROOT.TBranch object ("SPheno_GammaTotal_~sL") at 0x2cdc4a0>
<ROOT.TBranch object ("SPheno_Mass_~cL") at 0x2cdd090>
<ROOT.TBranch object ("SPheno_GammaTotal_~cL") at 0x2cddc60>
<ROOT.TBranch object ("SPheno_Mass_~b1") at 0x2cde850>
<ROOT.TBranch object ("SPheno_GammaTotal_~b1") at 0x2cdf420>
<ROOT.TBranch object ("SPheno_Mass_~t1") at 0x2ce0010>
<ROOT.TBranch object ("SPheno_GammaTotal_~t1") at 0x2ce0be0>
<ROOT.TBranch object ("SPheno_Mass_~eL") at 0x2ce17d0>
<ROOT.TBranch object ("SPheno_GammaTotal_~eL") at 0x2ce23a0>
<ROOT.TBranch object ("SPheno_Mass_~nueL") at 0x2ce2f90>
<ROOT.TBranch object ("SPheno_GammaTotal_~nueL") at 0x2ce3b80>
<ROOT.TBranch object ("SPheno_Mass_~muL") at 0x2ce4770>
<ROOT.TBranch object ("SPheno_GammaTotal_~muL") at 0x2ce5360>
<ROOT.TBranch object ("SPheno_Mass_~numuL") at 0x2ce5f50>
<ROOT.TBranch object ("SPheno_GammaTotal_~numuL") at 0x2ce6b40>
<ROOT.TBranch object ("SPheno_Mass_~tau1") at 0x2ce7730>
<ROOT.TBranch object ("SPheno_GammaTotal_~tau1") at 0x2ce8320>
<ROOT.TBranch object ("SPheno_Mass_~nutauL") at 0x2ce8f10>
<ROOT.TBranch object ("SPheno_GammaTotal_~nutauL") at 0x2ce9b00>
<ROOT.TBranch object ("SPheno_Mass_~dR") at 0x2cea6f0>
<ROOT.TBranch object ("SPheno_GammaTotal_~dR") at 0x2ceb2c0>
<ROOT.TBranch object ("SPheno_Mass_~uR") at 0x2cebeb0>
<ROOT.TBranch object ("SPheno_GammaTotal_~uR") at 0x2ceca80>
<ROOT.TBranch object ("SPheno_Mass_~sR") at 0x2ced670>
<ROOT.TBranch object ("SPheno_GammaTotal_~sR") at 0x2cee240>
<ROOT.TBranch object ("SPheno_Mass_~cR") at 0x2ceee30>
<ROOT.TBranch object ("SPheno_GammaTotal_~cR") at 0x2cefa00>
<ROOT.TBranch object ("SPheno_Mass_~b2") at 0x2cf05f0>
<ROOT.TBranch object ("SPheno_GammaTotal_~b2") at 0x2cf11c0>
<ROOT.TBranch object ("SPheno_Mass_~t2") at 0x2cf1db0>
<ROOT.TBranch object ("SPheno_GammaTotal_~t2") at 0x2cf2980>
<ROOT.TBranch object ("SPheno_Mass_~eR") at 0x2cf3570>
<ROOT.TBranch object ("SPheno_GammaTotal_~eR") 0x2d20f00>
<ROOT.TBranch object ("SPheno_BR_~eL_to_~chi10_e") at 0x2d12c20>
<ROOT.TBranch object ("SPheno_BR_~eL_to_~chi20_e") at 0x2d13810>
<ROOT.TBranch object ("SPheno_BR_~tau1_to_~chi10_tau") at 0x2d14400>
<ROOT.TBranch object ("SPheno_BR_~tau2_to_~chi10_tau") at 0x2d14ff0>
<ROOT.TBranch object ("SPheno_BR_~tau2_to_~chi20_tau") at 0x2d15be0>
<ROOT.TBranch object ("SPheno_BR_~tau2_to_~chi1m_nutau") at 0x2d167d0>
<ROOT.TBranch object ("SPheno_BR_~tau2_to_~tau1_h0") at 0x2d173d0>
<ROOT.TBranch object ("SPheno_BR_~tau2_to_~tau1_Z0") at 0x2d17fc0>
<ROOT.TBranch object ("SPheno_BR_~g_to_~b1_bbar") at 0x2d18bb0>
<ROOT.TBranch object ("SPheno_BR_~g_to_~b2_bbar") at 0x2d197a0>
<ROOT.TBranch object ("SPheno_BR_~g_to_~t1_tbar") at 0x2d1a390>
<ROOT.TBranch object ("SPheno_BR_~g_to_~t2_tbar") at 0x2d1af80>
<ROOT.TBranch object ("SPheno_BR_~g_to_~uL_ubar") at 0x2d1bb70>
<ROOT.TBranch object ("SPheno_BR_~g_to_~uR_ubar") at 0x2d1c760>
<ROOT.TBranch object ("SPheno_BR_~g_to_~dL_dbar") at 0x2d1d350>
<ROOT.TBranch object ("SPheno_BR_~g_to_~dR_dbar") at 0x2d1df40>
<ROOT.TBranch object ("SPheno_BR_~g_to_~b1bar_b") at 0x2d1eb30>
<ROOT.TBranch object ("SPheno_BR_~g_to_~b2bar_b") at 0x2d1f720>
<ROOT.TBranch object ("SPheno_BR_~g_to_~t1bar_t") at 0x2d20310>
<ROOT.TBranch object ("SPheno_BR_~g_to_~t2bar_t") at 0x2d20f00>
<ROOT.TBranch object ("SPheno_BR_~g_to_~uLbar_u") at 0x2d21af0>
<ROOT.TBranch object ("SPheno_BR_~g_to_~uRbar_u") at 0x2d226e0>
<ROOT.TBranch object ("SPheno_BR_~g_to_~dLbar_d") at 0x2d232d0>
<ROOT.TBranch object ("SPheno_BR_~g_to_~dRbar_d") at 0x2d23ec0>
<ROOT.TBranch object ("SPheno_BR_~uL_to_~chi10_u") at 0x2d24ab0>
<ROOT.TBranch object ("SPheno_BR_~uL_to_~chi20_u") at 0x2d256a0>
<ROOT.TBranch object ("SPheno_BR_~uL_to_~chi1p_d") at 0x2d26290>
<ROOT.TBranch object ("SPheno_BR_~uL_to_~chi2p_d") at 0x2d26e80>
<ROOT.TBranch object ("SPheno_BR_~uR_to_~chi10_u") at 0x2d27a70>
<ROOT.TBranch object ("SPheno_BR_~uR_to_~chi20_u") at 0x2d28660>
<ROOT.TBranch object ("SPheno_BR_~uR_to_~chi1p_d") at 0x2d29250>
<ROOT.TBranch object ("SPheno_BR_~uR_to_~chi2p_d") at 0x2d29e40>
<ROOT.TBranch object ("SPheno_BR_~t1_to_~chi10_t") at 0x2d2aa30>
<ROOT.TBranch object ("SPheno_BR_~t1_to_~chi20_t") at 0x2d2b620>
<ROOT.TBranch object ("SPheno_BR_~t1_to_~chi1p_b") at 0x2d2c210>
<ROOT.TBranch object ("SPheno_BR_~t1_to_~chi2p_b") at 0x2d2ce00>
<ROOT.TBranch object ("SPheno_BR_~b1_to_~chi10_b") at 0x2d2d9f0>
<ROOT.TBranch object ("SPheno_BR_~b1_to_~chi20_b") at 0x2d2e5e0>
<ROOT.TBranch object ("SPheno_BR_~b1_to_~chi1m_t") at 0x2d2f1d0>
<ROOT.TBranch object ("SPheno_BR_~b1_to_~chi2m_t") at 0x2d2fdc0>
<ROOT.TBranch object ("SPheno_BR_~b1_to_~t1_Wm") at 0x2d309b0>
<ROOT.TBranch object ("SPheno_BR_~b2_to_~chi10_b") at 0x2d315a0>
<ROOT.TBranch object ("SPheno_BR_~b2_to_~chi20_b") at 0x2d32190>
<ROOT.TBranch object ("SPheno_BR_~b2_to_~chi1m_t") at 0x2d32d80>
<ROOT.TBranch object ("SPheno_BR_~b2_to_~chi2m_t") at 0x2d33970>
<ROOT.TBranch object ("SPheno_BR_~b2_to_~t1_Wm") at 0x2d34560>
<ROOT.TBranch object ("MassOfLSP_Value") at 0x2d35150>
<ROOT.TBranch object ("NeutralinoLSP") at 0x2d35d20>
<ROOT.TBranch object ("Preselection_Chi2") at 0x2d368a0>
<ROOT.TBranch object ("Preselection_CorrelatedChi2") at 0x2d37490>
<ROOT.TBranch object ("Preselection_Measurement_Mass_h0") at 0x2d38080>
<ROOT.TBranch object ("Preselection_Deviation_Mass_h0") at 0x2d38ca0>
<ROOT.TBranch object ("Preselection_Pull_Mass_h0") at 0x2d398a0>
<ROOT.TBranch object ("Preselection_Chi2_Mass_h0") at 0x2d3a490>
<ROOT.TBranch object ("Preselection_Measurement_Mass_H0") at 0x2d3b080>
<ROOT.TBranch object ("Preselection_Deviation_Mass_H0") at 0x2d3bca0>
<ROOT.TBranch object ("Preselection_Pull_Mass_H0") at 0x2d3c8a0>
<ROOT.TBranch object ("Preselection_Chi2_Mass_H0") at 0x2d3d490>
<ROOT.TBranch object ("Preselection_Measurement_Mass_~chi1p") at 0x2d3e080>
<ROOT.TBranch object ("Preselection_Deviation_Mass_~chi1p") at 0x2d3eca0>
<ROOT.TBranch object ("Preselection_Pull_Mass_~chi1p") at 0x2d3f8c0>
<ROOT.TBranch object ("Preselection_Chi2_Mass_~chi1p") at 0x2d404b0>
<ROOT.TBranch object ("Preselection_Measurement_BR_Bs_mu_mu") at 0x2c5e850>
<ROOT.TBranch object ("Preselection_Deviation_BR_Bs_mu_mu") at 0x2c5f470>
<ROOT.TBranch object ("Preselection_Pull_BR_Bs_mu_mu") at 0x2c60090>
<ROOT.TBranch object ("Preselection_Chi2_BR_Bs_mu_mu") at 0x2c60c80>
<ROOT.TBranch object ("Preselection_Measurement_BR_Bu_tau_nu") at 0x2c61870>
<ROOT.TBranch object ("Preselection_Deviation_BR_Bu_tau_nu") at 0x2c62490>
<ROOT.TBranch object ("Preselection_Pull_BR_Bu_tau_nu") at 0x2c630b0>
<ROOT.TBranch object ("Preselection_Chi2_BR_Bu_tau_nu") at 0x2d52530>
<ROOT.TBranch object ("Preselection_Measurement_Abs_Delta_Mass_Bs") at 0x2d52ff0>
<ROOT.TBranch object ("Preselection_Deviation_Abs_Delta_Mass_Bs") at 0x2d53c10>
<ROOT.TBranch object ("Preselection_Pull_Abs_Delta_Mass_Bs") at 0x2d54830>
<ROOT.TBranch object ("Preselection_Chi2_Abs_Delta_Mass_Bs") at 0x2d55450>
<ROOT.TBranch object ("PreselectionPassed") at 0x2d56070>
<ROOT.TBranch object ("LEO_Chi2") at 0x2d56c60>
<ROOT.TBranch object ("LEO_CorrelatedChi2") at 0x2d577c0>
<ROOT.TBranch object ("LEO_Measurement_Mass_h0") at 0x2d583b0>
<ROOT.TBranch object ("LEO_Deviation_Mass_h0") at 0x2d58fa0>
<ROOT.TBranch object ("LEO_Pull_Mass_h0") at 0x2d59b90>
<ROOT.TBranch object ("LEO_Chi2_Mass_h0") at 0x2d5a780>
<ROOT.TBranch object ("LEO_Measurement_Mass_H0") at 0x2d5b370>
<ROOT.TBranch object ("LEO_Deviation_Mass_H0") at 0x2d5bf60>
<ROOT.TBranch object ("LEO_Pull_Mass_H0") at 0x2d5cb50>
<ROOT.TBranch object ("LEO_Chi2_Mass_H0") at 0x2d5d740>
<ROOT.TBranch object ("LEO_Measurement_Mass_~chi1p") at 0x2d5e330>
<ROOT.TBranch object ("LEO_Deviation_Mass_~chi1p") at 0x2d5ef20>
<ROOT.TBranch object ("LEO_Pull_Mass_~chi1p") at 0x2d5fb10>
<ROOT.TBranch object ("LEO_Chi2_Mass_~chi1p") at 0x2d60700>
<ROOT.TBranch object ("LEO_Measurement_Mass_W") at 0x2d612f0>
<ROOT.TBranch object ("LEO_Deviation_Mass_W") at 0x2d61ee0>
<ROOT.TBranch object ("LEO_Pull_Mass_W") at 0x2d62ad0>
<ROOT.TBranch object ("LEO_Chi2_Mass_W") at 0x2d636a0>
<ROOT.TBranch object ("LEO_Measurement_BR_b_s_gamma") at 0x2d64270>
<ROOT.TBranch object ("LEO_Deviation_BR_b_s_gamma") at 0x2d64e60>
<ROOT.TBranch object ("LEO_Pull_BR_b_s_gamma") at 0x2d65a50>
<ROOT.TBranch object ("LEO_Chi2_BR_b_s_gamma") at 0x2d66640>
<ROOT.TBranch object ("LEO_Measurement_BR_Bs_mu_mu") at 0x2d67230>
<ROOT.TBranch object ("LEO_Deviation_BR_Bs_mu_mu") at 0x2d67e20>
<ROOT.TBranch object ("LEO_Pull_BR_Bs_mu_mu") at 0x2d68a10>
<ROOT.TBranch object ("LEO_Chi2_BR_Bs_mu_mu") at 0x2d69600>
<ROOT.TBranch object ("LEO_Measurement_BR_Bu_tau_nu") at 0x2d6a1f0>
<ROOT.TBranch object ("LEO_Deviation_BR_Bu_tau_nu") at 0x2d6ade0>
<ROOT.TBranch object ("LEO_Pull_BR_Bu_tau_nu") at 0x2d6b9d0>
<ROOT.TBranch object ("LEO_Chi2_BR_Bu_tau_nu") at 0x2d6c5c0>
<ROOT.TBranch object ("LEO_Measurement_Abs_Delta_Mass_Bs") at 0x2d6d1b0>
<ROOT.TBranch object ("LEO_Deviation_Abs_Delta_Mass_Bs") at 0x2d6ddd0>
<ROOT.TBranch object ("LEO_Pull_Abs_Delta_Mass_Bs") at 0x2d6e9d0>
<ROOT.TBranch object ("LEO_Chi2_Abs_Delta_Mass_Bs") at 0x2d6f5c0>
<ROOT.TBranch object ("LEO_Measurement_DiffSM_amu") at 0x2d701b0>
<ROOT.TBranch object ("LEO_Deviation_DiffSM_amu") at 0x2d70da0>
<ROOT.TBranch object ("LEO_Pull_DiffSM_amu") at 0x2d71990>
<ROOT.TBranch object ("LEO_Chi2_DiffSM_amu") at 0x2d72580>
<ROOT.TBranch object ("SCYNet_Chi2_8TeV") at 0x2d73170>
<ROOT.TBranch object ("SCYNet_Chi2_13TeV") at 0x2d73d60>
<ROOT.TBranch object ("SCYNet_Chi2_Total") at 0x2d74950>
<ROOT.TBranch object ("SModelSCalculator_RValue") at 0x2d75540>
<ROOT.TBranch object ("SModelSCalculator_DecompositionStatus") at 0x2d76130>
<ROOT.TBranch object ("SModelSCalculator_FileStatus") at 0x2d76d50>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_0_Weight") at 0x2d77940>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel0_FractionMissing") at 0x2d78560>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_0_FractionOutsideGrid") at 0x2d79190>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_1_Weight") at 0x2d79de0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel1_FractionMissing") at 0x2d7aa00>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_1_FractionOutsideGrid") at 0x2d7b630>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_2_Weight") at 0x2d7c280>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel2_FractionMissing") at 0x2d7cea0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_2_FractionOutsideGrid") at 0x2d7dad0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_3_Weight") at 0x2d7e720>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel3_FractionMissing") at 0x2d7f340>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_3_FractionOutsideGrid") at 0x2d7ff70>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_4_Weight") at 0x2d80bc0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel4_FractionMissing") at 0x2d817e0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_4_FractionOutsideGrid") at 0x2d82410>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_5_Weight") at 0x2d83060>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel5_FractionMissing") at 0x2d83c80>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_5_FractionOutsideGrid") at 0x2d848b0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_6_Weight") at 0x2d85500>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel6_FractionMissing") at 0x2d86120>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_6_FractionOutsideGrid") at 0x2d86d50>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_7_Weight") at 0x2d879a0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel7_FractionMissing") at 0x2d885c0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_7_FractionOutsideGrid") at 0x2d891f0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_8_Weight") at 0x2d89e40>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel8_FractionMissing") at 0x2d8aa60>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_8_FractionOutsideGrid") at 0x2d8b690>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_9_Weight") at 0x2d8c2e0>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel9_FractionMissing") at 0x2d8cf00>
<ROOT.TBranch object ("SModelSCalculator_UnusedModel_9_FractionOutsideGrid") at 0x2d8db30>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_0_Weight") at 0x2d8e780>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_1_Weight") at 0x2d8f3a0>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_2_Weight") at 0x2d8ffc0>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_3_Weight") at 0x2d90be0>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_4_Weight") at 0x2d91800>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_5_Weight") at 0x2d92420>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_6_Weight") at 0x2d93040>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_7_Weight") at 0x2d93c60>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_8_Weight") at 0x2d94880>
<ROOT.TBranch object ("SModelSCalculator_MissingConstraint_9_Weight") at 0x2d954a0>

<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_0_Weight") at 0x2d960c0>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_1_Weight") at 0x2d96d10>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_2_Weight") at 0x2d97960>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_3_Weight") at 0x2d985b0>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_4_Weight") at 0x2d99200>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_5_Weight") at 0x2d99e50>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_6_Weight") at 0x2d9aaa0>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_7_Weight") at 0x2d9b6f0>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_8_Weight") at 0x2d9c340>
<ROOT.TBranch object ("SModelSCalculator_ConstraintOutsideGrid_9_Weight") at 0x2d9cf90>
<ROOT.TBranch object ("SModelSCalculator_NumberOfUnusedModels") at 0x2d9dbe0>
<ROOT.TBranch object ("SModelSCalculator_NumberOfMissingConstraints") at 0x2d9e800>
<ROOT.TBranch object ("SModelSCalculator_NumberOfConstraintsOutsideGrid") at 0x2d9f420>
<ROOT.TBranch object ("SModelS_Chi2") at 0x2da0070>
<ROOT.TBranch object ("SModelS_CorrelatedChi2") at 0x2da0bd0>
<ROOT.TBranch object ("SModelS_Measurement_Rvalue") at 0x2da17c0>
<ROOT.TBranch object ("SModelS_Deviation_Rvalue") at 0x2da23b0>
<ROOT.TBranch object ("SModelS_Pull_Rvalue") at 0x2da2fa0>
<ROOT.TBranch object ("SModelS_Chi2_Rvalue") at 0x2da3b90>
<ROOT.TBranch object ("RequirementsFullfilled") at 0x2da4780>
<ROOT.TBranchElement object ("MassOfLSP_Name") at 0x2da5500>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_0_Bracket") at 0x2dd9bd0>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_0_TxName") at 0x2dda9a0>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_1_Bracket") at 0x2ddb770>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_1_TxName") at 0x2ddc540>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_2_Bracket") at 0x2ddd310>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_2_TxName") at 0x2dde0e0>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_3_Bracket") at 0x2ddeeb0>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_3_TxName") at 0x2ddfc80>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_4_Bracket") at 0x2de0a50>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_4_TxName") at 0x2de1820>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_5_Bracket") at 0x2de25f0>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_5_TxName") at 0x2de33c0>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_6_Bracket") at 0x2de4190>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_6_TxName") at 0x2de4f60>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_7_Bracket") at 0x2de5d30>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_7_TxName") at 0x2de6b00>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_8_Bracket") at 0x2de78d0>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_8_TxName") at 0x2de86a0>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_9_Bracket") at 0x2de9470>
<ROOT.TBranchElement object ("SModelSCalculator_UnusedModel_9_TxName") at 0x2dea240>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_0_Bracket") at 0x2deb010>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_1_Bracket") at 0x2debde0>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_2_Bracket") at 0x2decbb0>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_3_Bracket") at 0x2ded980>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_4_Bracket") at 0x2dee750>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_5_Bracket") at 0x2def520>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_6_Bracket") at 0x2df02f0>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_7_Bracket") at 0x2df10c0>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_8_Bracket") at 0x2df1e90>
<ROOT.TBranchElement object ("SModelSCalculator_MissingConstraint_9_Bracket") at 0x2df2c60>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_0_Bracket") at 0x2df3a30>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_1_Bracket") at 0x2df4830>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_2_Bracket") at 0x2df5630>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_3_Bracket") at 0x2df63d0>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_4_Bracket") at 0x2df7230>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_5_Bracket") at 0x2df8030>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_6_Bracket") at 0x2df8e30>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_7_Bracket") at 0x2df9c30>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_8_Bracket") at 0x2dfaa30>
<ROOT.TBranchElement object ("SModelSCalculator_ConstraintOutsideGrid_9_Bracket") at 0x2dfb830>
<ROOT.TBranchElement object ("Error") at 0x2dfc630>
<ROOT.TBranchElement object ("Terminator") at 0x2dfd340>
<ROOT.TBranch object ("Chi2") at 0x2dfe050>
<ROOT.TBranch object ("IterationCounter") at 0x2dfeb90>
<ROOT.TBranch object ("PointAccepted") at 0x2dff780>
'''
