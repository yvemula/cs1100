# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:19:21 2022

@author: Yathin Vemula
"""

# Function that checks weather a given word is present in word frequency dictionary or not.
def found(word):
    return word in word_frequency


# Function that drops 1 or 2 characters from a given word to generate new words.
# Returns list of new words that are present in the word frequency dictionary.
def drop(word):
    result = []
    for i in range(len(word)):
        for j in range(i, len(word)):
            new_word = ""
            for k in range(len(word)):
                if k != i and k != j:
                    new_word += word[k]
            if new_word in word_frequency:
                result.append(new_word)
    return result


# Function that inserts characters at different indices of a given word to generate new words.
# Returns list of new words that are present in the word frequency dictionary.
def insert(word):
    result = []
    for i in range(len(word)+1):
        for char in "abcdefghijklmnopqrstuvxyz":
            new_word = word[:i] + char + word[i:]
            if new_word in word_frequency:
                result.append(new_word)
    return result


# Function that swaps consecutive characters of a given word to generate new words.
# Returns list of new words that are present in the word frequency dictionary.
def swap(word):
    result = []
    for i in range(len(word)-1):
        word_chars = [char for char in word]
        word_chars[i], word_chars[i+1] = word_chars[i+1], word_chars[i]
        new_word = "".join(char for char in word_chars)
        if new_word in word_frequency:
            result.append(new_word)
    return result


# Function that replaces characters of a given word from the keyboard dictionary to generate new words.
# Returns list of new words that are present in the word frequency dictionary.
def replace(word):
    result = []
    for i in range(len(word)):
        word_chars = [char for char in word]
        curr_char = word_chars[i]
        for replacement in keyboard[curr_char]:
            word_chars[i] = replacement
            new_word = "".join(word_chars)
            if new_word in word_frequency:
                result.append(new_word)
    return result


# Read input_words.txt file
with open("input_words.txt", "r") as f:
    file_data = f.read()
input_words = file_data.split("\n")

# Read keyboard.txt file
with open("keyboard.txt", "r") as f:
    file_data = f.read()
keyboard = {}
for line in file_data.split("\n"):
    chars = line.split(" ")
    keyboard[chars[0]] = chars[1:]

# Read words_10percent.txt file
with open("words_10percent.txt") as f:
    file_data = f.read()
word_frequency = {}
for line in file_data.split("\n"):
    word, frequency = line.split(",")
    word_frequency[word] = float(frequency)

# Iterate on each input word.
for word in input_words:
    # If word is found in word frequency dictionary then print the word and continue.
    if found(word):
        print("'{}' found in dictionary".format(word))
        print()
        continue
    
    # If word is not found, call "drop", "insert", "swap" and "replace" functions and join their results.
    results = drop(word) + insert(word) + swap(word) + replace(word)
    
    # Remove duplicates from the results.
    results = list(set(results))
    
    # Sort results in decreasing order of their frequencies and for each frequency in lexicographical order.
    results = sorted(results, key=lambda r: (word_frequency[r], r), reverse=True)
    
    # Pick the results having top 3 distinct frequencies.
    last_freq = None
    final_result = []
    count = 0
    for r in results:
        if word_frequency[r] != last_freq:
            count += 1
        
        if count > 3:
            break

        final_result.append(r)
        last_freq = word_frequency[r]
        
    # Print the output.
    output = ", ".join(final_result)
    print("'{}' not found in dictionary".format(word))
    print("Words generated from '{}' are :".format(word, output))
    print()