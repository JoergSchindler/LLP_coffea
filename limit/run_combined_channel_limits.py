import subprocess
import glob
import os

combined_path = "/uscms/home/jschindl/nobackup/HNL/LLP_coffea/limit/combine/HNL_datacards/combined_channel_v2/"
combined_path_out = "/uscms/home/jschindl/nobackup/HNL/LLP_coffea/limit/combine/HNL_datacards/combined_channel_v2/limits/"

for card in [os.path.basename(x) for x in glob.glob(combined_path+"*.txt")]:
    print(card)
    codeline = "combine -M AsymptoticLimits {odir}{name} -n _{name} --setParameters norm={norm} --freezeParameter norm ".format(name=card,odir=combined_path,norm=1)
    print(codeline)
    subprocess.call([codeline], shell = True)
    move_result = "mv higgsCombine_%s.AsymptoticLimits.mH120.root %s"%(card,combined_path_out)
    print(move_result)
    subprocess.call([move_result], shell = True)
    
                  
