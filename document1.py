"""
Author : Jyotsna Namdeo Nakte jnn2078
This code takes the document file 17170-0.txt that finds frequency of all the words in the document.
Then plots the grap taking their log frequencies.
Use Python nltk package stopwords and finds frequency of the words and plots them.
"""
from __future__ import division
import math
from math import log
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

#method that counts the number of words frequency in the orginal document
def to_count_words():
    #dictionary that keeps count of most frequent word
    most_frequent_words={}
    #command to open file
    open_file= open('17170-0.txt','r')
    #command that reads the file
    words_to_convert_stringgs = open_file.read()
    #command that finds all the words using regular expression package in python
    words=re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)',words_to_convert_stringgs)

    #loop that counts the word with frequencies
    for word in words:
        count = most_frequent_words.get( word, 0 )
        most_frequent_words[word] = count + 1
    #sorting the frequencies from low to high
    words_frequency_sorting = sorted( most_frequent_words.items(), key=lambda x: x[1] )
    #prints the sorted
    print("List that displays with frequencies in ascending order")
    print( words_frequency_sorting )
    #list of words
    names = []
    #list of their values
    values = []
    #list that keeps values of the log
    thevalues=[]
    #list of the rank numbers
    rank=[]

    # creates list of keys as labels and values as gear ratio for plotting
    for i, j in words_frequency_sorting:
        names.append( i )
        values.append( j )

    #loop that finds log values of frequencies
    for x in range(len(values)):
        foundvalues=math.log10(values[x])
        #ranksvalues=math.log10()
        thevalues.append(foundvalues)

    #loop that finds log values of rank
    for r in range(1,len(values)+1):
        ranksvalues = math.log10(r)
        rank.append(ranksvalues)
    #sorting the rank values
    rank.sort( reverse=True )
    #command printing all values
    print("The log of frequencies of words :")
    print(thevalues)
    print("Printing the log of ranks of the words:")
    print(rank)
    print("Printing the number of words:")
    print(len(values))

    #plots the log of rank by log of frequency of values
    plt.plot( rank, thevalues )
    # labels provided to the graph
    #labelling the axes
    plt.ylabel( 'log10Rank' )
    plt.xlabel( 'Log10(f)' )
    # saves the image of the graph
    #saving the graph
    plt.savefig( 'loggraphd1.png' )
    # displays the graph
    plt.show()



#function that counts frequency of the words without stop words
def to_count_words_without_stop():
    # dictionary that keeps count of most frequent word
    most_frequent_words = {}
    # command to open file

    #set of the stop words applied
    stop_words_to_apply = set( stopwords.words( 'english' ) )
    stop_words_to_apply.add( 'The' )
    #command opens the file to read command
    open_file = open( '17170-0.txt', 'r' )
    #command to read the file
    words_to_convert_stringgs = open_file.read()
    #finding all the words using findall function
    #words=words_to_convert_stringgs.split()
    words=re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)',words_to_convert_stringgs)
    #loop that checks if the words are in stopwords list it ignores and takes the rest
    for i in words:
        if not i in stop_words_to_apply:
            #commands that appends words  without stop words and keeps frequency count
            count = most_frequent_words.get( i, 0 )
            most_frequent_words[i] = count + 1

    words_frequency_sorting = sorted( most_frequent_words.items(), key=lambda x: x[1] )
    # prints the words with frequency ascending order
    print( "Printing the values without stop words in ascending order frequencies:" )
    print( words_frequency_sorting )
    # list that has words
    names = []
    # list for the values frequency
    values = []
    # list to store log of frequencies
    thevalues = []
    # list to store log of ranks
    rank = []
    # creates list of frequencies and names of word
    for i, j in words_frequency_sorting:
        names.append( i )
        values.append( j )
    # loop finding log of the frequenncy of words
    for x in range( len( values ) ):
        foundvalues = math.log10( values[x] )
        # ranksvalues=math.log10()
        thevalues.append( foundvalues )
    # loop finding the log of ranks
    for r in range( 1, len( values ) + 1 ):
        ranksvalues = math.log10( r )
        rank.append( ranksvalues )
    # sorting rank
    rank.sort( reverse=True )
    # printing the values
    print( "The log of frequencies of words :" )
    print( thevalues )
    print( "The log of ranks:" )
    print( rank )
    print( "The number of words removing stop words:" )
    print( len( values ) )
    # plotting the graphs
    plt.plot( rank, thevalues )
    # labels provided to the graph axes
    plt.ylabel( 'log10Rank' )
    plt.xlabel( 'Log10(f)' )
    # saves the image of the graph
    plt.savefig( 'stopwordgraphd1.png' )
    # displays the graph
    plt.show()


#main method
def main():
    to_count_words()
    to_count_words_without_stop()

if __name__ == '__main__':
    main()