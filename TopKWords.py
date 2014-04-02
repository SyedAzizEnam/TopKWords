#Top K words
#Copyright (C) 
#Author: S.Aziz Enam

"""
A function that returns the most frequent words in a txt file.
The script runs in O(n) time where n is the number of documents.
More specifically the algorithm runs in O(n+k*lg(k)) where k is the
number of requested frequent words. However, assuming that k will be
relativley small compared to n we can simplify to O(n).

The function reads the input and stores the result in a dictionary.
The function then uses a variation of the Quickselect algorithm to return
the top k unordered words in O(n) expected time. The function then uses a
heap to sort the k elements according to frequency count. Then finally the
words with the same frequency are ordered alphabetically.
"""
import random
import util
from Maxheap import Maxheap

def TopKWords(FILE, k):
    """
    :param FILE: The input file as a string that should be located in the
        same directory as the script.
    :param k: The number of most frequent words that need to be returned.
    
    :Output sortedwrdcnt: A list of the k most frequent words. If parameters
    are inputed improperlly an empty list is returned.

    Example input: ("file.txt",5)
            output: ['a','zed','i','you']
    """
    
    sortedwrdcnt= []
    
    Punctuations = [".",",","!","?",":",";","-"]

    if not k>0:
        print "ERROR: # OF REQUESTED WORDS MUST BE POSITIVE"
        return sortedwrdcnt
    try:
        f = open(FILE)
    except IOError:
        print "ERROR: FILE NOT FOUND."
        return sortedwrdcnt
    
    wordcount={}
    
    while(f):
        sentence = f.readline().strip().lower().split()
        if not sentence:
            break
        filtered_sentence = [w for w in sentence if not w in Punctuations]
        for word in filtered_sentence:
            if word[-1] in Punctuations:
                word = word[:-1]
            if word in wordcount:
                wordcount[word]+=1
            else:
                wordcount[word] = 1
            
    if not wordcount:
        print "ERROR: FILE IS EMPTY CONTAINS NO WORDS"
        return sortedwrdcnt
    
    if k>len(wordcount):
        print("ERROR: # OF REQUESTED WORDS EXCEEDS # OF DISTINCT WORDS IN INPUT FILE")
        return sortedwrdcnt
    
    wrdcnt=[]
    
    for wrd,cnt in wordcount.items():
        wrdcnt.append((cnt,wrd))

    topkwrdcnt =  Maxheap(util.selectTopK(wrdcnt,k,0,len(wrdcnt)))
 
    for i in range(k):
        sortedwrdcnt.append(topkwrdcnt.pop())

    sortedwrdcnt = util.alphabeticalorder(sortedwrdcnt)

    return [w for (c,w) in sortedwrdcnt]

