import spacy
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
from text_lib.config_var import *
nlp=spacy.load('en_core_web_lg')

# filter of extra words
extra_word=list(STOP_WORDS) + list(punctuation) + list("\n") + list("|||||")

def gen_freq_file(file_path):
    # read the file
    text_file=open(file_path)
    raw_text=text_file.read()
    text_file.close()

    # generate word token from file
    file_token=nlp(raw_text)
    tokens=[]
    for token in file_token:
        tokens.append(token.text)

    # make score for local file
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


# generates summary of file name called as long_local_file 
# given the scores to be local_token_score
def gen_summary (long_local_file, local_token_score, summary_word_count):
    print ("summary_word_count = " + str(summary_word_count))
    # read the file
    text_file=open(long_local_file)
    raw_text=text_file.read()
    text_file.close()

    # generate nlp output
    doc=nlp(raw_text)

    # generate sentence token from file
    sentence_token=[]
    for i in doc.sents:
        sentence_token.append(i)

    # generate sentence_token_score
    sentence_token_score={}
    for i in sentence_token:
        for j in i:
            lower_word=j.text.lower()
            if lower_word not in extra_word:
                if i in sentence_token_score.keys():
                    # not the first word of sentence
                    sentence_token_score[i]+=local_token_score[lower_word]
                else:
                    # first word of sentence
                    sentence_token_score[i]=local_token_score[lower_word]
    
    print ("--------")
    print (sentence_token_score)
    print ("--------")

    summary_sentences_1=nlargest(summary_word_count, sentence_token_score, key=sentence_token_score.get)
    

    summary_sentences_2=[]
    for i in summary_sentences_1:
        text_i = str(i)
        if text_i != "" and text_i != "\n":
            summary_sentences_2.append(text_i)

    summary_text="".join(str(i) for i in summary_sentences_2)

    return summary_text

def get_ref_summary(file_path):
    # read the file
    text_file=open(file_path)
    raw_text=text_file.read()
    text_file.close()

    return raw_text

# input: text in paragraph form
# output: tokens of text
def token_gen(raw_text):
    file_token=nlp(raw_text)
    tokens=[]
    for token in file_token:
        tokens.append(token.text)

    return tokens