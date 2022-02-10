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

print ("generating file_freq")
for i in file_list:
    print ("file_freq i= " + str(i))
    local_file_path=str(sys.argv[1]) + "/" + str(i)
    file_freq[local_file_path]=gen_freq_file(local_file_path)
print ("calculated file_freq")

print ("generating global_token_score")
global_token_score=gen_global_token_score(file_freq)
print ("calculated global_token_score")
rouge=Rouge()
# print first line of excel sheet
print("local_file_weight, local_file, rouge-1 f1-score, rouge-1 precision, rouge-1 recall,rouge-2 f1-score, rouge-2 precision, rouge-2 recall, rouge-l f1-score, rouge-l precision, rouge-l recall")
for local_file_weight in list(range(1,sum_local_global_file_weight+1,1)):
    for local_file in file_list:
        long_local_file=str(sys.argv[1]) + "/" + local_file
        local_token_score=gen_local_token_score(local_file_weight, long_local_file, file_freq, global_token_score)
        
        # generate summary based on score calculated in local_token_score for each file
        local_file_summary=gen_summary(long_local_file, local_token_score)
        # print(local_file_summary)

        # reference summary
        ref_summary_file=str(sys.argv[2]) + "/" + local_file
        ref_summary=get_ref_summary(ref_summary_file)
        # print("ref_summary= " + str(ref_summary))

        # generate metrics
        # ROUGE SCORE
        rouge_score=rouge.get_scores(local_file_summary, ref_summary)
        rouge_score=rouge_score[0]
        print(
            str(local_file_weight) + "," + 
            str(local_file) + "," + 
            str(rouge_score["rouge-1"]["f"]) + "," + 
            str(rouge_score["rouge-1"]["p"]) + "," + 
            str(rouge_score["rouge-1"]["r"]) + "," + 
            str(rouge_score["rouge-2"]["f"]) + "," + 
            str(rouge_score["rouge-2"]["p"]) + "," + 
            str(rouge_score["rouge-2"]["r"]) + "," + 
            str(rouge_score["rouge-l"]["f"]) + "," + 
            str(rouge_score["rouge-l"]["p"]) + "," + 
            str(rouge_score["rouge-l"]["r"])
        )
