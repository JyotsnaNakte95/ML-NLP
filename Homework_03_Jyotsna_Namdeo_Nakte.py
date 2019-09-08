"""
Author : Jyotsna Namdeo Nakte jnn2078
This code takes three files find their LDA , LSI models and finds inverted index of document using text, and one of the model
"""
#dependencies
from __future__ import division
import sys
import math
from math import log
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.parse.stanford import StanfordParser
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import re
'''
Method that takes the three text as the input
returns the document in string
'''
def input_data(file1,file2,file3):
    #file one
    document1=open(file1, 'r').read()
    #file two
    document2=open(file2, 'r').read()
    #file three
    document3=open(file3, 'r').read()
    return document1,document2,document3
'''
Method for Cleaning the text 
'''
def tokenize_clean_text(documents):
    #list of words
    words=[]
    wordsss=[]
    #command for tokenizer
    tokenizer = RegexpTokenizer( r'\w+' )
    #command for stemmer
    stemmer = PorterStemmer()
    #set of all stop words
    stop_words_to_apply = set( stopwords.words( 'english' ) )
    #data list of list with stemming
    data = []
    #data list of list without stemming of words
    data_without_stem=[]
    #loop of file in documents
    for file in documents:
        #loop for each file in list
        for i in file:
            #converting the word to lower case
            word = i.lower()
            #tokenizing the words
            tokens = tokenizer.tokenize( word )
            #command of list without stop words
            without_stop_words = [i for i in tokens if not i in stop_words_to_apply]
            #loop to find the total number of words in list
            for k in without_stop_words:
                if k not in words:
                    words.append(k)
            #stemming the words in the list
            data_without_stem.append(without_stop_words)
            #stemming of the words in data
            stemmed_words = [stemmer.stem( i ) for i in without_stop_words]
            for l in stemmed_words:
                if l not in wordsss:
                    wordsss.append(l)
            #data of the formed words
            data.append( stemmed_words )
    #returns the data of stemmed words, data without stemming, words list in all three documents
    return data,words,data_without_stem,wordsss

'''
Method of building the models LSI and LDA
'''
def build_models(data):
    #building the dictionary
    dictionary = corpora.Dictionary( data)
    #building the corpus
    corpus = [dictionary.doc2bow( text ) for text in data]
    #geneism lda model used
    ldamodel = gensim.models.ldamodel.LdaModel( corpus, num_topics=3, id2word=dictionary, passes=20 )
    #ldx=[x[0]for x in ldamodel.show_topic(1)]
    print("LDA Model:")
    print( ldamodel.print_topics( num_topics=3, num_words=10 ) )
    #finding topics of the lda model
    lda_words=[]
    for i in range(3):
        ldx = [x[0] for x in ldamodel.show_topic( i)]
        lda_words+=ldx
    #geneism package lsi model
    lsimodel = gensim.models.lsimodel.LsiModel( corpus, num_topics=3, id2word=dictionary )
    #printing lsi model
    print("LSI Model:")
    print( lsimodel.print_topics( num_topics=3, num_words=10 ) )
    return lda_words
'''
Method finding inverted index of document  in text
'''

def inverted_index_document_hg(dict,words):
    #dictionary of the text
    inverted={}
    #loop in words list
    for word in words:
        #set of the documents
        listo = set()
        #iterator of dictionary
        for key, values in dict.items():
            #if word present in document condition
            if word in values:
                #adds it in the set
                listo.add(key)
        #append to the list
        inverted[word]=listo
    print( "Inverted index for the text:" )
    print( inverted )
    return inverted

'''
Method of finding inverted index using lda model
'''
def find_for_lda_model(lda_words,inverted):
    #dictionary of inverted index on lda model
    inverted_lda={}
    #words in lda model
    for i in lda_words:
        #finding the word in dictionary
        u=inverted.get(i)
        #retrieving the values
        inverted_lda[i]=u
    #printing the inverted index of lda model
    print("Inverted index for model LDA:")
    print(inverted_lda)

'''
Method of the main program
'''
def main():
    #input files
    file1='17170-0.txt'
    file2='pg17606.txt'
    file3='Vegetius.txt'
    #documents in string returned
    document1, document2, document3=input_data(file1,file2,file3)
    doc=[document1,document2,document3]
    #creating list of list of documents
    documents=[[document1],[document2],[document3]]
    #print(documents)
    #cleaning of the text files:tokenizing, removing stop words, stemming
    data,words,data_without_stem,wordsss=tokenize_clean_text(documents)
    #building the models
    lda_words=build_models(data)
    #creating dictionary of the text
    dict_with_stem={"document_1":data[0],"document_2":data[1],"document_3":data[2]}
    #finding the inverted index of the document using text files
    inverted=inverted_index_document_hg( dict_with_stem, wordsss )
    #inverted index for lda model
    find_for_lda_model(lda_words, inverted)
if __name__ == '__main__':
    main()