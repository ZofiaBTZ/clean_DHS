import csv
import re
from collections import defaultdict
path = "//home/b/zbaran/Documents/Genf/Malawi-SNF/process_DHS/clean_DHS/python/TGMR61FL.MAP"
#read in the path as an arg
with open(path) as f:
    content = f.readlines()

dhs_recode = {}
var = ""
desc = ""
for line in content:
    if ('MV' in line[0:2]) or ('SM' in line[0:2]):
        line = re.sub('  +',', ',line)
        line = line.strip().split(', ')
        var = line[0]
        desc = line[1]
        print var + ', ' + desc
        var_dict = {}
        dhs_recode[var] ={ "desc":desc, "recode":var_dict}
    else:
        if not(var == ""):
            line = re.sub('  +',', ',line)
            level = line.strip().split(',')
            if len(level) > 1:
                print level[1] + '  ' + level[2]
                var_dict[level[1]]=level[2]
