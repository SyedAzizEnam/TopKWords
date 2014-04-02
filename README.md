TopKWords
=========

A function that returns the most frequent words in a txt file.
The script runs in O(n) time where n is the number of words in the document.
More specifically the algorithm runs in O(n+k*lg(k)) where k is the
number of requested frequent words. However, assuming that k will be
relativley small compared to n we can simplify to O(n).
