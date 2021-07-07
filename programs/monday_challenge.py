
def alphasort(sentence):
    words=sentence.split()
    words.sort()
    words= set(words) #or unique_words=set(words)
    return words  

##string=input("Enter words here:")
##print (alphasort(string))
