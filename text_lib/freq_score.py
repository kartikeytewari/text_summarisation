import spacy
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
from text_lib.config_var import *
nlp=spacy.load('en_core_web_lg')

def gen_freq_file(file_path):
    # read the file
    text_file=open(file_path)
    raw_text=text_file.read()
    text_file.close()

    # generate token from file
    file_token=nlp(raw_text)
    tokens=[]
    for token in file_token:
        tokens.append(token.text)

    # filter of extra words and word_freq
    extra_word=list(STOP_WORDS) + list(punctuation) + list("\n")
    word_freq={}
    for word in file_token:
        word_key=word.text.lower()
        if word_key not in extra_word:
            if word_key not in word_freq.keys():
                word_freq[word_key]=1
            else:
                word_freq[word_key]+=1

    return word_freq

def gen_global_token_score (file_freq):
    global_token_score={}
    for local_file in file_freq.keys():
        for i in file_freq[local_file].keys():
            if i in global_token_score:
                global_token_score[i]+=file_freq[local_file][i]
            else:
                global_token_score[i]=file_freq[local_file][i]
    
    return global_token_score

def gen_local_token_score(local_file_weight, local_file, file_freq, global_token_score):
    global_file_weight=sum_local_global_file_weight-local_file_weight
    local_token_score={}
    for i in file_freq[local_file]:
        local_token_score[i] = (local_file_weight*file_freq[local_file][i]) + (global_file_weight*global_token_score[i])

    return local_token_score

