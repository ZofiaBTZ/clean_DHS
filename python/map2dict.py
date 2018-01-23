import csv
import re

path = "//home/b/zbaran/Documents/Genf/Malawi-SNF/process_DHS/clean_DHS/python/TGMR61FL.MAP"
with open(path) as f:
    content = f.readlines()

for line in content:
#    print(line)
    if 'MV' in line:
        line = re.sub('   +',',',line)
        print line
