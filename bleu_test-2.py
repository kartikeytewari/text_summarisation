# two references for one document
from nltk.translate.bleu_score import sentence_bleu
from datasets import load_metric

references = [['this', 'is', 'a', 'book'], ['this', 'is' 'test']]
candidates = ['this', 'is', 'a', 'test']
print ("nltk 1-gram bleu score = " + str(sentence_bleu(references, candidates, weights=(1, 0, 0, 0))))
print ("nltk 2-gram bleu score = " + str(sentence_bleu(references, candidates, weights=(0, 1, 0, 0))))
print ("nltk 3-gram bleu score = " + str(sentence_bleu(references, candidates, weights=(0, 0, 1, 0))))
print ("nltk 4-gram bleu score = " + str(sentence_bleu(references, candidates, weights=(0, 0, 0, 1))))

bleu = load_metric("bleu")
references = [[['this', 'is', 'a', 'book'], ['this', 'is' 'test']]]
predictions = [['this', 'is', 'a', 'test']]
score=bleu.compute(predictions=predictions, references=references)

print ("datasets bleu = " + str(score["bleu"]))
print ("datasets precisions 1-gram = " + str(score["precisions"][0]))
print ("datasets precisions 2-gram = " + str(score["precisions"][1]))
print ("datasets precisions 3-gram = " + str(score["precisions"][2]))
print ("datasets precisions 4-gram = " + str(score["precisions"][3]))

print ("datasets brevity penalty = " + str(score["brevity_penalty"]))
print ("datasets length_ratio = " + str(score["length_ratio"]))
print ("datasets translation_length = " + str(score["translation_length"]))
print ("datasets reference_length = " + str(score["reference_length"]))
