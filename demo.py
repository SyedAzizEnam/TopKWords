from TopKWords import*

k=25

FILE= "file2.txt"

def main():

    words= TopKWords(FILE, k)

    print ("The Top " + str(k) + " words in " + FILE + " are :")
    print words

main()
