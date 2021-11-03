import spacy
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
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

    print(word_freq)
