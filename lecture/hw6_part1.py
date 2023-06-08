# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:06:54 2022

@author: Yathin Vemula
"""

import re

file1 = input("Enter the first file to analyze and compare ==> ")
file2 = input("Enter the second file to analyze and compare ==> ")
max_sep = int(
    input("Enter the maximum separation between words in a pair ==> "))
    
# 10 - 15 line of code reads a file and replaces all new line character with spaces
# Then replacing apostrophe with null space(that is removing apostrophe)
# Then splits the whole string into a list(splits when encounters space)
with open('stop.txt', 'r') as file:
    s3 = file.read().replace("\n", " ").replace("'", "").split()
with open(file1, 'r') as file:
    s1 = file.read().replace("\n", " ").split()
with open(file2, 'r') as file:
    s2 = file.read().replace("\n", " ").split()

wordListFile1 = []
wordListFile2 = []
# alpha is mentioning only letters friom a to z and A to Z are allowed
# removing numbers and special characters and leaving rest of the alphabets as it is
alpha = re.compile('[^a-zA-Z]')
for i in s1:
    s = alpha.sub('', i)
    if s != '':
        wordListFile1.append(s.lower())
for i in s2:
    s = alpha.sub('', i)
    if s != '':
        wordListFile2.append(s.lower())

# This code is in a for loop to remove stop words from very large words else the code misbehaves
for i in range(10):
    for i in wordListFile1:
        if i in s3:
            wordListFile1.remove(i)
    for i in wordListFile2:
        if i in s3:
            wordListFile2.remove(i)


# File 1
print("Evaluating document {0}".format(file1))
# Average word length
totalLength = 0
for i in wordListFile1:
    totalLength += len(i)
avgWordLength1 = round(
    totalLength / len(wordListFile1), 2)
print("1. Average word length:", avgWordLength1)

# Ratio of distinct to total words
distinctWordsFile1 = set(wordListFile1)
ratio = 1.000
ratio = len(distinctWordsFile1)/len(wordListFile1)
print("2. Ratio of distinct words to total words: {:.3f}".format(ratio))

# Word sets for document
lengthDictWordsFile1 = {}
for i in set(wordListFile1):
    if len(i) in lengthDictWordsFile1:
        lengthDictWordsFile1[len(i)].append(i)
    else:
        lengthDictWordsFile1[len(i)] = []
        lengthDictWordsFile1[len(i)].append(i)

print("3. Word sets for document {0}:".format(file1))
for i in range(1, 1 + max(lengthDictWordsFile1.keys())):
    if i not in lengthDictWordsFile1:
        print(" " + str(i) + ": 0: ")
    else:
        print(" " + str(i)+": " +
              str(len(lengthDictWordsFile1[i])) + ": " + " ".join(sorted(lengthDictWordsFile1[i])))

# Word pairs for document
pairs = []
print("3. Word pairs for document {0}:".format(file1))

for i in range(len(wordListFile1)):
    for j in range(i + 1, max_sep + i + 1):
        try:
            pair = [wordListFile1[i], wordListFile1[j]]
            pairs.append(" ".join(sorted(pair)))
        except:
            pass
pairs = sorted(pairs)
distinctPairs1 = sorted(set(pairs))
print("  {0} distinct pairs".format(len(distinctPairs1)))
print(" ", distinctPairs1[0])
print(" ", distinctPairs1[1])
print(" ", distinctPairs1[2])
print(" ", distinctPairs1[3])
print(" ", distinctPairs1[4])
print("  ...")
print(" ", distinctPairs1[-5])
print(" ", distinctPairs1[-4])
print(" ", distinctPairs1[-3])
print(" ", distinctPairs1[-2])
print(" ", distinctPairs1[-1])

# Ratio of distinct word pairs to total
ratio = len(distinctPairs1)/len(pairs)
print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratio))
print()


# File 2
print("Evaluating document {0}".format(file2))
# Average word length
totalLength = 0
for i in wordListFile2:
    totalLength += len(i)
avgWordLength2 = round(
    totalLength / len(wordListFile2), 2)
print("1. Average word length:", avgWordLength2)

# Ratio of distinct to total words
distinctWordsFile2 = set(wordListFile2)
ratio = 1.000
ratio = len(distinctWordsFile2)/len(wordListFile2)
print("2. Ratio of distinct words to total words: {:.3f}".format(ratio))

# Word sets for document
lengthDictWordsFile2 = {}
for i in set(wordListFile2):
    if len(i) in lengthDictWordsFile2:
        lengthDictWordsFile2[len(i)].append(i)
    else:
        lengthDictWordsFile2[len(i)] = []
        lengthDictWordsFile2[len(i)].append(i)

print("3. Word sets for document {0}:".format(file2))
for i in range(1, 1 + max(lengthDictWordsFile2.keys())):
    if i not in lengthDictWordsFile2:
        print(" " + str(i) + ": 0: ")
    else:
        print(" " + str(i)+": " +
              str(len(lengthDictWordsFile2[i])) + ": " + " ".join(sorted(lengthDictWordsFile2[i])))

# Word pairs for document
pairs = []
print("3. Word pairs for document {0}:".format(file2))

for i in range(len(wordListFile2)):
    for j in range(i + 1, max_sep + i + 1):
        try:
            pair = [wordListFile2[i], wordListFile2[j]]
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
print("Summary Comparison")

# 1. ex1.txt on average uses longer words than ex2.txt
if avgWordLength1 > avgWordLength2:
    print("1. "+file1+" on average uses longer words than "+file2)
else:
    print("1. "+file2+" on average uses longer words than "+file1)

# 2. Overall word use similarity: 0.154
bothSetFile = set(wordListFile1+wordListFile2)
similarity = 0
for i in set(wordListFile1):
    if i in set(wordListFile2):
        similarity += 1
print("2. Overall word use similarity: {:.3f}".format(
      round(similarity/(len(bothSetFile)), 3)))

# 3. Word use similarity by length:
print("3. Word use similarity by length:")
for i in range(1, 1 + max(max(lengthDictWordsFile1.keys()), max(lengthDictWordsFile2.keys()))):
    if i in lengthDictWordsFile1 and i in lengthDictWordsFile2:
        similarity = 0
        for j in lengthDictWordsFile1[i]:
            if j in lengthDictWordsFile2[i]:
                similarity += 1
        bothSetFile = set(lengthDictWordsFile1[i]+lengthDictWordsFile2[i])
        print(" "+str(i) +
              ": {:.4f}".format(round(similarity / len(bothSetFile), 4)))
    else:
        print(" "+str(i)+": 0.0000")

# 4. Word pair similarity: 0.0833
similarity = 0
bothSetFile = set(distinctPairs1+distinctPairs2)
for i in distinctPairs1:
    if i in distinctPairs2:
        similarity += 1
print("4. Word pair similarity: {:.4f}".format(
      round(similarity/(len(bothSetFile)), 4)))