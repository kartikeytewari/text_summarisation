#! /usr/bin/env python3
import sys
import os
from pprint import pprint
from text_lib.freq_score import *
from text_lib.config_var import *
from rouge import Rouge

# genrate token for all files
folder=sys.argv[1]
file_freq={}
file_list=list(os.walk(folder))[0][2]
file_list.sort()
for i in file_list:
    local_file_path=str(sys.argv[1]) + "/" + str(i)
    file_freq[local_file_path]=gen_freq_file(local_file_path)

global_token_score=gen_global_token_score(file_freq)
rouge=Rouge()
for local_file_weight in list(range(1,sum_local_global_file_weight+1,1)):
    print("----------------------")
    print("")
    print("local_file_weight = " + str(local_file_weight))
    for local_file in file_list:
        long_local_file=str(sys.argv[1]) + "/" + local_file
        local_token_score=gen_local_token_score(local_file_weight, long_local_file, file_freq, global_token_score)
        
        print("local_file= " + str(local_file))
        # generate summary based on score calculated in local_token_score for each file
        local_file_summary=gen_summary(long_local_file, local_token_score)
        # print(local_file_summary)

        # reference summary
        ref_summary_file=str(sys.argv[2]) + "/" + local_file
        ref_summary=get_ref_summary(ref_summary_file)
        # print("ref_summary= " + str(ref_summary))

        # generate metrics
        # ROUGE SCORE
        pprint(rouge.get_scores(local_file_summary, ref_summary))
        print("")
    print("----------------------")