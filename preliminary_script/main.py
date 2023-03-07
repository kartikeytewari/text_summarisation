#! /usr/bin/env python3
import spacy
import sys
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

nlp=spacy.load('en_core_web_lg')

def print_summary(raw_text, summary_text):
    print(summary_text)

    print("length of original text = " + str(len(raw_text)))
    print("length of summary text = " + str(len(summary_text)))

# define the text to summarise
text_file=open(sys.argv[1])
raw_text=text_file.read()
text_file.close()

# tokenise the text
doc=nlp(raw_text)

# generate tokens
tokens=[]
for token in doc:
    tokens.append(token.text)

# generate word list to filtered out
extra_word=list(STOP_WORDS) + list(punctuation) + list("\n")

# generate word frequency
word_freq={}
for word in doc:
    word_key=word.text.lower()
    if word_key not in extra_word:
        if word_key not in word_freq.keys():
            word_freq[word_key]=1
        else:
            word_freq[word_key]+=1


# make normalised frequency
max_freq=max(word_freq.values())
for word in word_freq.keys():
    word_freq[word]/=max_freq

# generate list of sentence_token
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
                sentence_token_score[i]+=word_freq[lower_word]
            else:
                sentence_token_score[i]=word_freq[lower_word]

select_length=int(len(sentence_token)*0.3)
summary_1=nlargest(select_length, sentence_token_score, key=sentence_token_score.get)

summary_2=[]
for i in summary_1:
    summary_2.append(i.text)

summary_3 = " ".join((summary_2))
print_summary(raw_text, summary_3)
