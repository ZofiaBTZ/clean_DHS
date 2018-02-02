import csv
import re
import argparse
from collections import defaultdict

def map2dict(map_file, var_levels, var_names, words):
    with open(map_file) as f:
        content = f.readlines()
        
    dhs_recode = {}
    dhs_recode_rev = {}
    var = ""
    desc = ""
    print words[0]
    for line in content:
        line = re.sub('\(m\)', '', line)
        line = re.sub('\(', '', line)
        line = re.sub('\)', '', line)
        if (('MV' in line[0:2]) or ('SM' in line[0:2]) or ('MG' in line[0:2]) ): 
            if not(var == ""):
                dhs_recode[var] ={ "desc":desc, "recode":var_dict}
                dhs_recode_rev[var] ={ "desc":desc, "recode":var_dict_rev}
            line = re.sub('  +',', ',line)
            line = line.strip().split(', ')
            var = line[0]
            desc = line[1]
            #print var + ', ' + desc
            var_dict = {}
            var_dict_rev = {}
        else:
            if not(var == ""):
                line = re.sub('  +',', ',line)
                level = line.strip().split(',')
                if len(level) > 1:
                    #print level[1] + '  ' + level[2]
                    var_dict[level[1]]=level[2]
                    var_dict_rev[level[2]]=level[1]

        #print dhs_recode['MV130']['desc']
        #print dhs_recode['MV130']['recode']

    with open(var_levels, 'w+') as f:
        for key, value in dhs_recode.items() :
            if any((word in value['desc']) for word in words) \
               and ('NA - ' not in value['desc']):
                for key1, value1 in value['recode'].items():
                    f.write(key + ' ,' + value['desc']+ ', ' + key1 + ' , ' + value1 + '\n')

    with open(var_names, 'w+') as f:
        for key, value in dhs_recode.items() :
            if (any(word in value['desc']) for word in words) \
               and ('NA - ' not in value['desc']):
                f.write(key +' , ' + value['desc'] + '\n')


def main():
    parser = argparse.ArgumentParser(description='Process DHS .MAP file into a .csv file. Usage: map2dict')
    parser.add_argument('--map_file',action = "store",  
                        help='.MAP DHS file to be processed')

    parser.add_argument('--var_names', action = "store",
                        help='path and a name of the .csv file with short and long variables names to be store ')

    parser.add_argument('--var_levels', action = "store", 
                        help='path and a name of the .csv file with levels of variables')

    parser.add_argument('--words', action = "store",
                        help='list of words in \" \". The variables, which description has any of these words, will be included')

    args = parser.parse_args()
    map_file = args.map_file
    var_levels = args.var_levels
    var_names = args.var_names
    words = args.words.split(" ")
    map2dict(map_file, var_levels, var_names, words)



main()
