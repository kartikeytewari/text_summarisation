#! /usr/bin/env python3
import sys
import os
from pprint import pprint
from text_lib.freq_score import *
from text_lib.config_var import *

# genrate token for all files
folder=sys.argv[1]
file_freq={}
file_list=list(os.walk(folder))[0][2]
for i in file_list:
    local_file_path=str(sys.argv[1]) + "/" + str(i)
    file_freq[local_file_path]=gen_freq_file(local_file_path)

print(file_freq)
global_token_score=gen_global_token_score(file_freq)
for local_file_weight in list(range(1,sum_local_global_file_weight+1,1)):
    for local_file in file_list:
        long_local_file=str(sys.argv[1]) + "/" + local_file
        local_token_score=gen_local_token_score(local_file_weight, long_local_file, file_freq, global_token_score)
        print("----------------------")
        print("local_file_weight = " + str(local_file_weight))
        print("local_file = " + str(local_file))
        print("global_token_score = " + str(global_token_score))
        print("file_freq[long_local_file] = " + str(file_freq[long_local_file]))
        print("local_token_score = " + str(local_token_score))
        print("----------------------")
