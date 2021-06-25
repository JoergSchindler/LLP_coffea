#!/usr/bin/env python
import json
import gzip
import uproot3 as uproot
import numexpr
import numpy as np
from coffea import hist, lookup_tools
from coffea.util import load, save
from coffea.hist import plot


corrections = {}

with uproot.open("data/pileUp_Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.root") as fin_pileup:
    norm = lambda x: x / x.sum()
    #print(fin_pileup["pileup"].values)
    #print(fin_pileup["pileup"].values.sum())
    data_pu = norm(fin_pileup["pileup"].values)
    data_pu_puUp = norm(fin_pileup["pileup_plus"].values)
    data_pu_puDown = norm(fin_pileup["pileup_minus"].values)

    # https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2018_25ns_JuneProjectionFull18_PoissonOOTPU_cfi.py
    mc_pu = np.array([
        4.695341e-10, 1.206213e-06, 1.162593e-06, 6.118058e-06, 1.626767e-05,
        3.508135e-05, 7.12608e-05, 0.0001400641, 0.0002663403, 0.0004867473,
        0.0008469, 0.001394142, 0.002169081, 0.003198514, 0.004491138,
        0.006036423, 0.007806509, 0.00976048, 0.0118498, 0.01402411,
        0.01623639, 0.01844593, 0.02061956, 0.02273221, 0.02476554,
        0.02670494, 0.02853662, 0.03024538, 0.03181323, 0.03321895,
        0.03443884, 0.035448, 0.03622242, 0.03674106, 0.0369877,
        0.03695224, 0.03663157, 0.03602986, 0.03515857, 0.03403612,
        0.0326868, 0.03113936, 0.02942582, 0.02757999, 0.02563551,
        0.02362497, 0.02158003, 0.01953143, 0.01750863, 0.01553934,
        0.01364905, 0.01186035, 0.01019246, 0.008660705, 0.007275915,
        0.006043917, 0.004965276, 0.004035611, 0.003246373, 0.002585932,
        0.002040746, 0.001596402, 0.001238498, 0.0009533139, 0.0007282885,
        0.000552306, 0.0004158005, 0.0003107302, 0.0002304612, 0.0001696012,
        0.0001238161, 8.96531e-05, 6.438087e-05, 4.585302e-05, 3.23949e-05,
        2.271048e-05, 1.580622e-05, 1.09286e-05, 7.512748e-06, 5.140304e-06,
        3.505254e-06, 2.386437e-06, 1.625859e-06, 1.111865e-06, 7.663272e-07,
        5.350694e-07, 3.808318e-07, 2.781785e-07, 2.098661e-07, 1.642811e-07,
        1.312835e-07, 1.081326e-07, 9.141993e-08, 7.890983e-08, 6.91468e-08,
        6.119019e-08, 5.443693e-08, 4.85036e-08, 4.31486e-08, 3.822112e-08
    ])
    mask = mc_pu > 0.
    corr = data_pu.copy()
    corr_puUp = data_pu_puUp.copy()
    corr_puDown = data_pu_puDown.copy()
    corr[mask] /= mc_pu[mask]
    corr_puUp[mask] /= mc_pu[mask]
    corr_puDown[mask] /= mc_pu[mask]
    pileup_corr = lookup_tools.dense_lookup.dense_lookup(corr, fin_pileup["pileup"].edges)
    pileup_corr_puUp = lookup_tools.dense_lookup.dense_lookup(corr_puUp, fin_pileup["pileup"].edges)
    pileup_corr_puDown = lookup_tools.dense_lookup.dense_lookup(corr_puDown, fin_pileup["pileup"].edges)

corrections['2018_pileupweight'] = pileup_corr
corrections['2018_pileupweight_puUp'] = pileup_corr_puUp
corrections['2018_pileupweight_puDown'] = pileup_corr_puDown

with uproot.open("./WPT.root") as f:
    wpt_LO = f['Wpt']
with uproot.open("./dyturbo_cms/wp-13tev-cms.root") as f:
    wpt_NLO = f['s_qt']

wpt_NLO_normalized = wpt_NLO.values/wpt_NLO.values.sum()

ptrange = slice(np.searchsorted(wpt_LO.edges, 25.), np.searchsorted(wpt_LO.edges, 800.) + 1)
corrections['wpt'] = lookup_tools.dense_lookup.dense_lookup( wpt_NLO_normalized[ptrange] /wpt_LO.values[ptrange] , wpt_LO.edges[ptrange])

save(corrections, 'corrections.coffea')
