from coffea import hist
import numpy as np

cutflow_axis =  hist.Bin('cutFlow','cutFlow',20,0,20)
nMinus1_axis =  hist.Bin('Nminus1','i-th cut',20,0,20)

histograms ={
            "nCluster": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Cat("region", "region"),
                hist.Bin("nCluster", "nCluster", 4, 0, 4),
                cutflow_axis,
            ),                   
            "nCluster_dt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Cat("region", "region"),
                hist.Bin("nCluster", "nCluster", 4, 0, 4),
                cutflow_axis,
            ),                   
            "nCluster_n-1": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("nCluster", "nCluster", 4, 0, 4),
                nMinus1_axis,
            ),                   
            "accept": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("gLLP_csc", "gLLP_csc", 2, 0, 2),
                hist.Bin("gLLP_dt", "gLLP_dt", 2, 0, 2),
            ),                   
            "ClusterSize": hist.Hist("Events",hist.Cat("dataset", "Dataset"),   
                hist.Cat("region", "region"),
                hist.Bin("ClusterSize", r"$N_{rechits}$", 50, 0, 2000),
            ),  
            "ClusterTime": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Cat("region", "region"),
                hist.Bin("ClusterTime", "ClusterTime", 40, -100, 100),
            ),   
            "dphi_cluster_csc": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Cat("region", "region"),                                          
                hist.Bin("ClusterSize", r"$N_{rechits}$", 100, 0, 1000),
                hist.Bin("dphi_lep", r'$\Delta\phi$(cluster,lep)', 30, 0, np.pi),
                hist.Bin("dphi_MET", r'$\Delta\phi$(cluster,MET)', 30, 0, np.pi),
            ), 
            "ClusterSize_dt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),   
                hist.Cat("region", "region"),
                hist.Bin("ClusterSize", r"$N_{rechits}$", 50, 0, 2000),
            ),  
            "ClusterTime_dt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Cat("region", "region"),
                hist.Bin("ClusterBx", "Cluster Bx", 20, -10, 10),
            ),   
            "dphi_cluster_dt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Cat("region", "region"),                                          
                hist.Bin("ClusterSize", r"$N_{rechits}$", 100, 0, 1000),
                hist.Bin("dphi_lep", r'$\Delta\phi$(cluster,lep)', 30, 0, np.pi),
                hist.Bin("dphi_MET", r'$\Delta\phi$(cluster,MET)', 30, 0, np.pi),
            ), 
            ## reco var.
            "nLeptons": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("nLeptons", "nLeptons", 5, 0, 5),
            ),            
            "elePt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("elePt", "elePt", 40, 0, 100),
            ), 
            "eleEta": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("eleEta", "eleEta", 40, -5, 5),
            ),             
            "muPt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("muPt", "muPt", 40, 0, 100),
            ), 
            "muEta": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("muEta", "muEta", 40, -5, 5),
            ),             

            "nJets": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("nJets", "nJets", 5, 0, 5),
            ),
            "jetPt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Cat("region", "region"),                                   
                hist.Bin("jetPt", "jetPt", 50, 50, 300),
            ),          
            "jetMet_dPhi": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Bin("jetMet_dPhi", "jetMet_dPhi", 30, -np.pi, np.pi),
            ), 
            "metXYCorr": hist.Hist("Events",hist.Cat("dataset", "Dataset"),
                hist.Cat("region", "region"),                                   
                hist.Bin("metXYCorr", "metXYCorr", 50, 0, 500),
            ),
            "MT": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Cat("region", "region"),                            
                hist.Bin("MT", "MT", 50, 0, 200),
            ),
            ## Event var            
            "nPU": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("nPU", "nPU", 100, 0, 100),
            ),            
            "nPU_noweight": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("nPU", "nPU", 100, 0, 100),
            ),            
            "gWPt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("gWPt", "gWPt", 50,0,500),
            ),            
            "gWPt_noweight": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("gWPt", "gWPt", 50,0,500),
            ),           
            ## gen var.
            "glepdPhi": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("gLLP_lepdPhi", r'$\Delta\phi$(gLLP,g_lep)', 30, 0,np.pi),
            ),                    
            "gLepPt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("gLepPt", 'gLepPt', 50, 0,500),
            ),                    
            "gLLP_e": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("gLLP_e", 'gLLP_e', 50, 0,500),
            ),   
            "gLLP_pt": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("gLLP_pt", 'gLLP_pt', 50, 0,500),
            ),   
            "gLLP_eta": hist.Hist("Events",hist.Cat("dataset", "Dataset"),                
                hist.Bin("gLLP_eta", 'gLLP_eta', 40, -5,5),
            ),   
}
