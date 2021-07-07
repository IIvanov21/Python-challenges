

def compare_words(word1,word2):
    m=0
    for i in word2:
        if i in word1: m+=1
    if m==len(word2): return True
    else: return False
           
if __name__ == "__main__":
    w1=input("Enter first word:")
    w2=input("Enter second word:")

    print (compare_words(w1,w2))
