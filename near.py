def CompareWords(word1,word2):
    count={word1[i]:0 for i in range(len(word1))}
    for i in range(len(word1)): count[word1[i]]+=1

    for i in range(len(word2)):
        if(count.get(word2[i])== None or count[word2[i]]== 0): return False
        count[word2[i]] -= 1
    return True

w1=input("Enter first word:")
w2=input("Enter second word:")

print (CompareWords(w1,w2))
