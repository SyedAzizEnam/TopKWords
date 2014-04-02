"""
A Max Heap object created by using an existing implementaion of
Min Heap in heapq.py. 
"""
import heapq
class Maxheap:
    def __init__(self,x):
        """
        :param x: a list of tuples (c,w) where c is count and w is a word
        """
        self.heap = [(-c,w)for (c,w) in x]
        heapq.heapify(self.heap)
    def push(self,item):
        (c,w) = item
        heapq.heappush(self.heap, (-c,w))
    def pop(self):
        (c,w)=heapq.heappop(self.heap)
        return (-c,w)
