from coffea import hist
import numpy as np

nMinus1_axis =  hist.Bin('Nminus1','i-th cut',20,0,20)
dataset_axis = hist.Cat("dataset", "Dataset")
cutFlow_axis = hist.Cat("cutflow", "cutflow")
region_axis  = hist.Cat("region", "region")
syst_axis  = hist.Cat("syst", "syst")
wpt_axis = hist.Bin("gWPt","W Pt[GeV]",
            np.array([   0.,    5.,   10.,   15.,   20.,   25.,   30.,   35.,   40.,
                        45.,   50.,   60.,   70.,   80.,   90.,  100.,  125.,  150.,
                        200.,  300.,  800., 1500.]))
histograms ={
            "cutflow": hist.Hist("Events",dataset_axis, region_axis, cutFlow_axis),
            "nCluster": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("nCluster", "nCluster", 4, 0, 4)
            ),                   
            "nCluster_dt": hist.Hist("Events",dataset_axis,region_axis,
                hist.Bin("nCluster", "nCluster", 4, 0, 4)
            ),                   
            "nCluster_n-1": hist.Hist("Events",dataset_axis,                
                hist.Bin("nCluster", "nCluster", 4, 0, 4)
            ),                   
            "accept": hist.Hist("Events",dataset_axis,                
                hist.Bin("gLLP_csc", "gLLP_csc", 2, 0, 2),
                hist.Bin("gLLP_dt", "gLLP_dt", 2, 0, 2),
            ),
            ### CSC clusters                   
            "ClusterSize": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterSize", r"$N_{rechits}$", 50, 0, 2000),
            ),  
            "ClusterTime": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterTime", "ClusterTime", 40, -100, 100),
            ),
            "ClusterEta": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterEta", "ClusterEta", 40, -5, 5),
            ),
            "ClusterAvgStation10": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterAvgStation10", "ClusterAvgStation10", 20, 0, 5),
            ),
            "ClusterNStation10": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterNStation10", "ClusterNStation10", 5, 0, 5),
            ),
            "ClusterME11_12": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterME11_12", "n ME11/ME12", 20, 0, 20),
            ),
            "ClusterTimeSpread": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterTimeSpread", "ClusterTimeSpread[ns]", 20, 0, 40),
            ),
            "ClusterJetVetoPt": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterJetVetoPt", "Matched Jet Pt[GeV]", 50, 0, 100),
            ),
            "ClusterMuonVetoPt": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterMuonVetoPt", "Matched Muon Pt[GeV]", 50, 0, 100),
            ),
       
            "dphi_cluster_csc": hist.Hist("Events",dataset_axis,
                region_axis,                                          
                hist.Bin("ClusterSize", r"$N_{rechits}$", 100, 0, 1000),
                hist.Bin("dphi_lep", r'$\Delta\phi$(cluster,lep)', 32, 0, 3.2),
                hist.Bin("dphi_MET", r'$\Delta\phi$(cluster,MET)', 32, 0, 3.2),
            ),
            "dphi_cluster_syst": hist.Hist("Events",dataset_axis,
                syst_axis,                                          
                hist.Bin("ClusterSize", r"$N_{rechits}$", 100, 0, 1000),
                hist.Bin("dphi_lep", r'$\Delta\phi$(cluster,lep)', 32, 0, 3.2),
            ), 
 
            "ClusterSize_dt": hist.Hist("Events",dataset_axis,   
                region_axis,
                hist.Bin("ClusterSize", r"$N_{rechits}$", 50, 0, 2000),
            ),  
            "ClusterTime_dt": hist.Hist("Events",dataset_axis,                
                region_axis,
                hist.Bin("ClusterBx", "Cluster Bx", 20, -10, 10),
            ),   
            "ClusterEta_dt": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterEta", "ClusterEta", 40, -5, 5),
            ),
            "ClusterAvgStation10_dt": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterAvgStation10", "ClusterAvgStation10", 20, 0, 5),
            ),
            "ClusterNStation10_dt": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterNStation10", "ClusterNStation10", 5, 0, 5),
            ),
            "ClusterMB1_dt": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterMB1", "number of MB1 hits", 20, 0, 20),
            ),
            "ClusterJetVetoPt_dt": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterJetVetoPt", "Matched Jet Pt[GeV]", 50, 0, 100),
            ),
            "ClusterMuonVetoPt_dt": hist.Hist("Events",dataset_axis, region_axis,
                hist.Bin("ClusterMuonVetoPt", "Matched Muon Pt[GeV]", 50, 0, 100),
            ),
            "Cluster_runNum_dt": hist.Hist("Events",dataset_axis,
                region_axis,                                          
                hist.Bin("ClusterSize", r"$N_{rechits}$", 50, 0, 500),
                hist.Bin("RunNumber", "RunNumber", 100, 272000, 276300), ## for 2016 BC
            ), 
            "Cluster_rz_dt": hist.Hist("Events",dataset_axis,
                region_axis,                                          
                hist.Bin("R", "R[cm]", 40, 400, 800),
                hist.Bin("Z", "Z[cm]", 100, -600 ,600), ## for 2016 BC
            ), 
            "Cluster_phi_dt": hist.Hist("Events",dataset_axis,
                region_axis,                                          
                hist.Bin("phi", "cluster phi", 64, -3.2, 3.2),
            ), 

            "dphi_cluster_dt": hist.Hist("Events",dataset_axis,
                region_axis,                                          
                hist.Bin("ClusterSize", r"$N_{rechits}$", 100, 0, 1000),
                hist.Bin("dphi_lep", r'$\Delta\phi$(cluster,lep)', 32, 0, 3.2),
                hist.Bin("dphi_MET", r'$\Delta\phi$(cluster,MET)', 32, 0, 3.2),
            ), 
            "dphi_cluster_dt_syst": hist.Hist("Events",dataset_axis,
                syst_axis,                                          
                hist.Bin("ClusterSize", r"$N_{rechits}$", 100, 0, 1000),
                hist.Bin("dphi_lep", r'$\Delta\phi$(cluster,lep)', 32, 0, 3.2),
            ), 

            ## reco var.
            "nLeptons": hist.Hist("Events",dataset_axis,
                hist.Bin("nLeptons", "nLeptons", 5, 0, 5),
            ),            
            "elePt": hist.Hist("Events",dataset_axis,
                hist.Bin("elePt", "elePt", 40, 0, 100),
            ), 
            "eleEta": hist.Hist("Events",dataset_axis,
                hist.Bin("eleEta", "eleEta", 40, -5, 5),
            ),             
            "muPt": hist.Hist("Events",dataset_axis,
                hist.Bin("muPt", "muPt", 40, 0, 100),
            ), 
            "muEta": hist.Hist("Events",dataset_axis,
                hist.Bin("muEta", "muEta", 40, -5, 5),
            ),             

            "nJets": hist.Hist("Events",dataset_axis,
                hist.Bin("nJets", "nJets", 5, 0, 5),
            ),
            "jetPt": hist.Hist("Events",dataset_axis,
                region_axis,                                   
                hist.Bin("jetPt", "jetPt", 50, 50, 300),
            ),          
            "jetMet_dPhi": hist.Hist("Events",dataset_axis,
                hist.Bin("jetMet_dPhi", "jetMet_dPhi", 30, -3.2, 3.2),
            ), 
            "metXYCorr": hist.Hist("Events",dataset_axis,
                region_axis,                                   
                hist.Bin("metXYCorr", r"$E_{T}^{miss}$ [GeV]", 50, 0, 500),
            ),
            "MT": hist.Hist("Events",dataset_axis,                
                region_axis,                            
                hist.Bin("MT", "MT", 50, 0, 200),
            ),
            ## Event var            
            "nPU": hist.Hist("Events",dataset_axis,                
                hist.Bin("nPU", "nPU", 100, 0, 100),
            ),            
            "nPU_noweight": hist.Hist("Events",dataset_axis,                
                hist.Bin("nPU", "nPU", 100, 0, 100),
            ),            
            "gWPt": hist.Hist("Events",dataset_axis, wpt_axis),
            "gWPt_noweight": hist.Hist("Events",dataset_axis, wpt_axis),           
            ## gen var.
            "glepdPhi": hist.Hist("Events",dataset_axis, region_axis, 
                hist.Bin("gLLP_lepdPhi", r'$\Delta\phi$(gLLP,g_lep)', 32, 0,32),
            ),                    
            "gLepPt": hist.Hist("Events",dataset_axis,                
                hist.Bin("gLepPt", 'gLepPt', 50, 0,500),
            ),                    
            "gLLP_e": hist.Hist("Events",dataset_axis,region_axis, 
                hist.Bin("gLLP_e", 'LLP energy[GeV]', 50, 0,500),
            ),   
            "gLLP_pt": hist.Hist("Events",dataset_axis,region_axis,    
                hist.Bin("gLLP_pt", 'LLP pT[GeV]', 50, 0,500),
            ),   
            "gLLP_eta": hist.Hist("Events",dataset_axis,region_axis,     
                hist.Bin("gLLP_eta", 'gLLP_eta', 40, -5,5),
            ),   
            "llp_cls_z":hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("llp_z", "LLP decay Z[cm]", 40, 570, 1050),                    
                hist.Bin("cluster_z", "cluster Z[cm]", 40, 570, 1050),                                                         
            ), 
            "llp_cls_eff_z":hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("selection",'pass/fail', 2,0,2),
                hist.Bin("z", "LLP decay Z[cm]", 50, 400, 1100),
            ),
            "llp_cls_eff_r":hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("selection",'pass/fail', 2,0,2),
                hist.Bin("r", "LLP decay R[cm]", 20, 100, 700),
            ),
            "llp_cls_eff_e":hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("selection",'pass/fail', 2,0,2),
                hist.Bin("e", "LLP E[GeV]", 20, 0, 250),
            ),
            "llp_cls_dt_eff_z":hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("selection",'pass/fail', 2,0,2),
                hist.Bin("z", "LLP decay Z[cm]", 35, 0, 700),
            ),
            "llp_cls_dt_eff_r":hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("selection",'pass/fail', 2,0,2),
                hist.Bin("r", "LLP decay R[cm]", 40, 200, 800),
            ),
            "llp_cls_dt_eff_e":hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("selection",'pass/fail', 2,0,2),
                hist.Bin("e", "LLP E[GeV]", 20, 0, 250),
            ),
}
