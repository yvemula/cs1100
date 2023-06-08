# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:06:54 2022
@author: Yathin Vemula
"""
import re

read_firstFile = input("Enter the first file to analyze and compare ==> ")
print(read_firstFile)
read_secondFile = input("Enter the second file to analyze and compare ==> ")
print(read_secondFile)
max_sep = int(input("Enter the maximum separation between words in a pair ==> "))
print(max_sep)
print()
# replaces all new line characters with spaces
# removes ' with a null space
# splits the string into a list
with open('stop.txt', 'r') as file:
    read3 = file.read().replace("\n", " ").replace("'", "").split()
with open(read_firstFile, 'r') as file:
    read1 = file.read().replace("\n", " ").split()
with open(read_secondFile, 'r') as file:
    read2 = file.read().replace("\n", " ").split()
wordList1 = []
wordList2 = []
# this removes numbers and special characters and leaving rest of the alphabets as it is
aphi = re.compile('[^a-zA-Z]')
for i in read1:
    s = aphi.sub('', i)
    if s != '':
        wordList1.append(s.lower())
for i in read2:
    s = aphi.sub('', i)
    if s != '':
        wordList2.append(s.lower())
# This code is in a for loop to remove stop words from very large words 
for i in range(10):
    for i in wordList1:
        if i in read3:
            wordList1.remove(i)
    for i in wordList2:
        if i in read3:
            wordList2.remove(i)
# File 1
print("Evaluating document {0}".format(read_firstFile))
# Average word length
lengthT = 0
for x in wordList1:
    lengthT += len(x)
wordLength1 = round(lengthT / len(wordList1), 2)
print("1. Average word length: {:.2f}".format(wordLength1))
# Ratio of distinct to total words
dWordsFile1 = set(wordList1)

rat = len(dWordsFile1)/len(wordList1)
print("2. Ratio of distinct words to total words: {:.3f}".format(rat))
# Word sets for document
lengthWordsFile11 = {}
for i in set(wordList1):
    if len(i) in lengthWordsFile11:
        lengthWordsFile11[len(i)].append(i)
    else:
        lengthWordsFile11[len(i)] = []
        lengthWordsFile11[len(i)].append(i)


print("3. Word sets for document {0}:".format(read_firstFile))
list_length1=[]
distinct_words1=set(wordList1)
for word in distinct_words1:
    list_length1.append(len(word))

for i in range(1, 1+max(list_length1)):
    if list_length1.count(i)==0:
        print("   {}:   {}:".format(i, list_length1.count(i)), end='')
    elif i==10:
        print("  {}:   {}: ".format(i, list_length1.count(i)), end='')
    elif list_length1.count(i)>=10:
        print("   {}:  {}: ".format(i, list_length1.count(i)), end='')
    else:
        print("   {}:   {}: ".format(i, list_length1.count(i)), end='')
    words1=[]
    for x in distinct_words1:
        if len(x)==i:
            words1.append(x)
    words_sorrted1=sorted(words1)
    if len(words_sorrted1)<7:
        print(" ".join(str(x) for x in words_sorrted1[:]))
    else:
        print(words_sorrted1[0],words_sorrted1[1],words_sorrted1[2],"...",words_sorrted1[-3],words_sorrted1[-2],words_sorrted1[-1])

# Word pairs for document
pairs = []
print("4. Word pairs for document {0}".format(read_firstFile))

for i in range(len(wordList1)):
    for j in range(i + 1, max_sep + i + 1):
        try:
            pair = [wordList1[i], wordList1[j]]
            pairs.append(" ".join(sorted(pair)))
        except:
            pass
pairs = sorted(pairs)
dPairs1 = sorted(set(pairs))
print("  {0} distinct pairs".format(len(dPairs1)))
print(" ", dPairs1[0])
print(" ", dPairs1[1])
print(" ", dPairs1[2])
print(" ", dPairs1[3])
print(" ", dPairs1[4])


# Ratio of distinct word pairs to total
ratio = len(dPairs1)/len(pairs)
print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratio))
print()


# File 2
print("Evaluating document {0}".format(read_secondFile))
# Average word length
totalLength = 0
for i in wordList2:
    totalLength += len(i)
avgWordLength2 = round(
    totalLength / len(wordList2), 2)
print("1. Average word length:", avgWordLength2)

# Ratio of distinct to total words
distinctWordsFile2 = set(wordList2)
ratio = 1.000
ratio = len(distinctWordsFile2)/len(wordList2)
print("2. Ratio of distinct words to total words: {:.3f}".format(ratio))

# Word sets for document
lengthDictWordsFile2 = {}
for i in set(wordList2):
    if len(i) in lengthDictWordsFile2:
        lengthDictWordsFile2[len(i)].append(i)
    else:
        lengthDictWordsFile2[len(i)] = []
        lengthDictWordsFile2[len(i)].append(i)

print("3. Word sets for document {0}:".format(read_secondFile))
list_length2=[]
distinct_words2=set(wordList2)
for word in distinct_words2:
    list_length2.append(len(word))

for i in range(1, 1+max(list_length2)):
    if list_length2.count(i)==0:
        print("   {}:   {}:".format(i, list_length2.count(i)), end='')
    elif i==10:
        print("  {}:   {}: ".format(i, list_length2.count(i)), end='')
    elif list_length2.count(i)>=10:
        print("   {}:  {}: ".format(i, list_length2.count(i)), end='')
    else:
        print("   {}:   {}: ".format(i, list_length2.count(i)), end='')
    words2=[]
    for x in distinct_words2:
        if len(x)==i:
            words2.append(x)
    sort_words2=sorted(words2)
    if len(sort_words2)<7:
        print(" ".join(str(x) for x in sort_words2[:]))
    else:
        print(sort_words2[0],sort_words2[1],sort_words2[2],"...",sort_words2[-3],sort_words2[-2],sort_words2[-1])

# Word pairs for document
pairs = []
print("4. Word pairs for document {0}".format(read_secondFile))

for i in range(len(wordList2)):
    for j in range(i + 1, max_sep + i+1):#deleted pkus one
        try:
            pair = [wordList2[i], wordList2[j]]
            pairs.append(" ".join(sorted(pair)))
        except:
            pass
pairs = sorted(pairs)
distinctPairs2 = sorted(set(pairs))
print("  {0} distinct pairs".format(len(distinctPairs2)))
print(" ", distinctPairs2[0])
print(" ", distinctPairs2[1])
print(" ", distinctPairs2[2])
print(" ", distinctPairs2[3])
print(" ", distinctPairs2[4])
print("  ...")
print(" ", distinctPairs2[-5])
print(" ", distinctPairs2[-4])
print(" ", distinctPairs2[-3])
print(" ", distinctPairs2[-2])
print(" ", distinctPairs2[-1])

# Ratio of distinct word pairs to total
ratio = len(distinctPairs2)/len(pairs)
print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratio))
print()

# Summary comparison
print("Summary comparison")

# 1. ex1.txt on average uses longer words than ex2.txt
if wordLength1 > avgWordLength2:
    print("1. "+read_firstFile+" on average uses longer words than "+read_secondFile)
else:
    print("1. "+read_secondFile+" on average uses longer words than "+read_firstFile)

# 2. Overall word use similarity: 0.154
bothSetFile = set(wordList1+wordList2)
similarity = 0
for i in set(wordList1):
    if i in set(wordList2):
        similarity += 1
print("2. Overall word use similarity: {:.3f}".format(
      round(similarity/(len(bothSetFile)), 3)))

# 3. Word use similarity by length:
print("3. Word use similarity by length:")
for i in range(1, 1 + max(max(lengthWordsFile11.keys()), max(lengthDictWordsFile2.keys()))):
    if i in lengthWordsFile11 and i in lengthDictWordsFile2:
        similarity = 0
        for j in lengthWordsFile11[i]:
            if j in lengthDictWordsFile2[i]:
                similarity += 1
        bothSetFile = set(lengthWordsFile11[i]+lengthDictWordsFile2[i])
        print("   "+str(i) +
              ": {:.4f}".format(round(similarity / len(bothSetFile), 4)))
    else:
        if i>9:
            print("  "+str(i)+": 0.0000")
        else:
            print("   "+str(i)+": 0.0000")

# 4. Word pair similarity: 0.0833
similarity = 0
bothSetFile = set(dPairs1+distinctPairs2)
for i in dPairs1:
    if i in distinctPairs2:
        similarity += 1
print("4. Word pair similarity: {:.4f}".format(
      round(similarity/(len(bothSetFile)), 4)))