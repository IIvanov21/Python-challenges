from os import read
import string

lines = []
subwords=[]
wordDic=dict.fromkeys(string.ascii_lowercase,[])
keys=wordDic.keys()
with open ("wordlist.txt") as f:
    for line in f:
        line=line.strip()
        if line!='' and line[0] in wordDic.keys():
            wordDic[line[0]].append(line)


def find_words(word):
    for j in range(len(word)):
        for i in lines:
            if word[:j]==i:
                subwords.append(i)
                word.replace(i,'')
                if word=='': break
                find_words(word)


#user_word=input("Enter word:")
#find_words(user_word)
for key, value in wordDic.items() :
    print (key, value[2])


         