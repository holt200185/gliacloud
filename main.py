import re
import string

document_text = open('raw_sentences.txt', 'r')

def ngram_probs(filename='raw_sentences.txt'):

    #to make lower case
    text_string = document_text.read()
    text_string = document_text.read().lower()

    #make match pattern for bigram case
    match_pattern = re.search(r'\bwe are\b', text_string)

    #bigram_probs =text_string.count('we','are')
    #trigram_probs =text_string.count('we','are','here')

    bigram_probs =match_pattern
    trigram_probs =match_pattern

    return bigram_probs, trigram_probs

cnt2, cnt3 = ngram_probs()

print(cnt2)
#print(cnt2[('we', 'are')])
