
def alphasort(sentence):
    words=sentence.split()
    words.sort()
    words= set(words) #or unique_words=set(words)
    return words  
if __name__ == "__main__":
    string=input("Enter words here:")
    print (alphasort(string))
