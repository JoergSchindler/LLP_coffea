import subprocess
from os.path import exists
ctau_points = [100,400,800,1000,2000,5000]
outdir = "./combine/HNL_datacards/combined_channel_v2/"
muonchannel_path ="./combine/HNL_datacards/muon_v22_new_pickle_testing/"
electron_channel_path ="./combine/HNL_datacards/ele_v16_new_pickle_testing/" 
tmp = []
problem_points = [
        (0.1,0.2,0.7),
        (0.1,0.3,0.6),
        (0.1,0.6,0.3),
        (0.1,0.7,0.2),
        (0.2,0.7,0.1),
        (0.3,0.6,0.1),
        (0.6,0.3,0.1),
        (0.7,0.2,0.1),
        ]
for fe in range(11):

    fe_float=fe/10.0


    for fmu in range(11):
        fmu_float=fmu/10.0


        for ftau in range(11):
            ftau_float=ftau/10.0

           
            if round(ftau_float+fmu_float+fe_float,1)!=1: continue
            if (fe_float,fmu_float,ftau_float) not in problem_points: continue
            for ctau in ctau_points:
                mixed_sample_name = "HNL_mixed-fe{:.1f}-fmu{:.1f}-ftau{:.1f}".format(float(fe_float),float(fmu_float),float(ftau_float)).replace(".","p")+"_mHNL2p0_pl{}_comb.txt".format(ctau)
                print(mixed_sample_name)
                if exists(electron_channel_path+mixed_sample_name) and exists(muonchannel_path+mixed_sample_name):
                    codeline = "python combination.py prefix1=%(prefix1)s prefix2=%(prefix2)s %(outcard)s"%({"prefix1":electron_channel_path+mixed_sample_name,
                                                                                                         "prefix2":muonchannel_path+mixed_sample_name,
                                                                                                         "outcard":outdir+mixed_sample_name}) 
                    print(codeline)
                    subprocess.call([codeline], shell = True)
                else:
                    if exists(electron_channel_path+mixed_sample_name):
                        print("File missing: ",muonchannel_path+mixed_sample_name)
                        tmp.append(muonchannel_path+mixed_sample_name)
                    else:
                        print("File missing: ",electron_channel_path+mixed_sample_name)
                        tmp.append(electron_channel_path+mixed_sample_name)


print(tmp)
print(len(tmp))

