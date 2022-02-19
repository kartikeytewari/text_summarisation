#! /usr/bin/env python3
import sys
import os
from pprint import pprint
from text_lib.freq_score import *
from text_lib.config_var import *
from rouge import Rouge
from datasets import load_metric

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
# print first line of excel sheet
print("local_file_weight, local_file, rouge-1 f1-score, rouge-1 precision, rouge-1 recall,rouge-2 f1-score, rouge-2 precision, rouge-2 recall, rouge-l f1-score, rouge-l precision, rouge-l recall")
for local_file_weight in list(range(1,sum_local_global_file_weight+1,1)):
    for local_file in file_list:
        
        # print logging information
        print ("local_file_weigh= " + str(local_file_weight))
        print ("local_file= " + str(local_file))

        long_local_file=str(sys.argv[1]) + "/" + local_file
        local_token_score=gen_local_token_score(local_file_weight, long_local_file, file_freq, global_token_score)
        
        # reference summary
        ref_summary_file=str(sys.argv[2]) + "/" + local_file
        ref_summary=get_ref_summary(ref_summary_file)
        # print("ref_summary= " + str(ref_summary))

        # generate summary based on score calculated in local_token_score for each file
        ref_summary_token_simple = token_gen(ref_summary)
        # local_file_summary=gen_summary(long_local_file, local_token_score, len(ref_summary_token_simple))
        local_file_summary=gen_summary(long_local_file, local_token_score, 10)
        # print(local_file_summary)

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

        local_file_summary_token = []
        local_file_summary_token.append(token_gen(local_file_summary))

        ref_summary_token_temp = []
        ref_summary_token_temp.append(token_gen(ref_summary))

        ref_summary_token = []
        ref_summary_token.append(ref_summary_token_temp)

        print ("")
        print ("ref_summary_token_simple length = " + str(len(ref_summary_token_simple)))
        print ("local_file_summary_token length = " + str(len(local_file_summary_token)))
        print ("ref_summary_token:")
        print (ref_summary_token)
        print ("")
        print ("local_file_summary_token:")
        print (local_file_summary_token)
        print ("")
        bleu=load_metric("bleu")
        print(bleu.compute(predictions=local_file_summary_token, references=ref_summary_token))
        print ("--------")
        print ("")
