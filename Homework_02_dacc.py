"""
Author : Jyotsna Namdeo Nakte jnn2078
This code takes the pre-processed document file finds the minimum and maximum length of the sentences in the text file.
The program even finds the mean, standard deviation of the file. Later, we then perform POS tagging on the longest sentence
"""
from __future__ import division
import sys
import math
from math import log
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.parse.stanford import StanfordParser
import matplotlib.pyplot as plt
from nltk.grammar import CFG
#tokenizer package from nltk toolkit
nltk.download('punkt')
#tagger package from nltk toolkit
nltk.download('averaged_perceptron_tagger')
#parser package from nltk toolkit
nltk.download('treebank')

'''
Method that reads the file document and stores it in dictionary with length
'''
def count_sentence_length(file):
    #list that takes the length of the sentences
    word_counts_sentence=[]
    #dictionary that stores sentence as keys and length as values
    dict_of_sentences={}
    # command to open file
    open_file = open( file, 'r' )
    # command that reads the file
    sentences_to_read = open_file.read()
    #tokenizer of the nltk package
    tokenizer = nltk.data.load( 'tokenizers/punkt/english.pickle' )
    #list that stores the tokens of sentences
    list_of_length=tokenizer.tokenize(sentences_to_read)
   # print(list_of_length)
    #loop that finds the length of sentence  and stores keys and values in dictionary
    for j in list_of_length:
        words = len( j )
        dict_of_sentences[j]= words
    #length of sentences stored in list
    for i in list_of_length:
        words = len(i)
        word_counts_sentence.append( words)
    #function returns dictionary, list of length
    return dict_of_sentences,word_counts_sentence
'''
Method that finds data of the sentences and text file
i.e., Mean, Standard Deviation, Minimum length of sentence, Maximum length of sentence
'''
def find_data(dict_of_sentences, words_sentences_count):
    #finds the minimum length of the sentences
    minimum=min(words_sentences_count)
    #finds the maximum length of the sentences
    maximum=max( words_sentences_count)
    #finds the mean of the sentences
    mean=np.mean(words_sentences_count)
    #finds the standard deviation of the sentences
    standard_deviation=np.std(words_sentences_count)
    #prints the minimum length
    print("Minimum length: "+str(minimum))
    #prints the maximum length
    print("Maximum length: "+str(maximum))
    #prints the mean
    print("Mean: "+str(mean))
    #prints the standard deviation
    print("Standard Deviation: "+str(standard_deviation))
    #function returns the minimum, maximum length
    return minimum,maximum
'''
Method that finds the parts of speech tagging on the sentences
'''
def performing_pos(dict_of_sentence,minimum,maximum):
    #loop that finds the sentence of minimum and maximum from dictionary
    for key,value in dict_of_sentence.items():
        if value==minimum:
            minimum_sentence=key
    print("Minimum sentence: "+minimum_sentence)
    for key,value in dict_of_sentence.items():
        if value==maximum:
            maximum_sentence=key
    print("Maximum sentence: "+maximum_sentence)
    #parts of speech tagging with help of nltk package
    tokens_minimum=nltk.word_tokenize(minimum_sentence)
    print("Parts of Speech tagging of minimum sentence: " + str(nltk.pos_tag(tokens_minimum)))
    tokens_maximum = nltk.word_tokenize( maximum_sentence )
    print( "Parts of Speech tagging of maximum sentence: " + str( nltk.pos_tag( tokens_maximum ) ) )

#main program that calls all the function
def main():
    file=sys.argv[1]
    dict_of_sentence, words_sentences_count =count_sentence_length(file)
    minimum,maximum=find_data(dict_of_sentence,words_sentences_count)
    performing_pos(dict_of_sentence,minimum,maximum)


if __name__ == '__main__':
    main()