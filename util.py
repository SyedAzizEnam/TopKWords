import random
import heapq

def selectTopK(wrdcnt,k,start,end):
    """
    :param wrdcnt: A list of tuples in the form (c,w) where w is the word
        and c is the count.
    :param k: Number of top elements requested.
    :param start: Start index of the list
    :param end: End index of the list + 1

    :Output: A list of the Top K elements in wrdcnt

    Example to search the whole list: selectTopK(wrdcnt,10,0,len(wrdcnt))
    """
    if (end-start)> 0:
        pivot= wrdcnt[random.randint(start,end-1)][0]

        smaller = []
        larger = []
        same = []
        for item in wrdcnt[start:end]:
            if item[0] <pivot:
                smaller.append(item)
            if item[0] == pivot:
                same.append(item)
            if item[0] > pivot:
                larger.append(item)

        same = alphabeticalorder(same)
        
        m = len(larger)+ len(wrdcnt[0:start])
        count = len(same)

        wrdcnt = wrdcnt[0:start] + larger + same + smaller
        if k>=m and k<=(m+count):
            return wrdcnt[:k]
        if m > k:
            return selectTopK(wrdcnt,k,start,m)
        else:
            return selectTopK(wrdcnt,k,m+count-1,len(wrdcnt))

    return wrdcnt[:k]

def alphabeticalorder(sortedwrdcnt):
    """
    :param sortedwrdcnt: A list already sorted by highest count
        and contains tuples of the form (c,w), where c is count
        w is word.

    :Output: An list sorted by frequency count and then by alphabetical order
    """
    
    i=0
    while(i<len(sortedwrdcnt)-1):
        
        if sortedwrdcnt[i][0]==sortedwrdcnt[i+1][0]:
            samecounts = []
            j=i
            while(j+1 < len(sortedwrdcnt) and sortedwrdcnt[j][0]==sortedwrdcnt[j+1][0]):
                samecounts.append(sortedwrdcnt[j])
                j+= 1    
            samecounts.append(sortedwrdcnt[j])
            
            heapq.heapify(samecounts)
            alphabeticalwords = sortedwrdcnt[0:i]
            
            for _ in range(len(samecounts)):
                alphabeticalwords.append(heapq.heappop(samecounts))
                
            sortedwrdcnt = alphabeticalwords + sortedwrdcnt[j+1:]
            i=j
            
        i+=1

    return sortedwrdcnt

        
