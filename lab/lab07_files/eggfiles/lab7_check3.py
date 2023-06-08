# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:03:19 2022

@author: Yathin Vemula
"""

def parse_line(text):
    t = None
    tempList = []
    slashIndex = []
    if text.count("/") < 3:
        return t
    else:
        i = len(text)
        count = 0
        while i > 0:
            if text[i-1] == '/':
                slashIndex.append(i-1)
                tempString = text[i: len(text)]
                count += 1
                tempList.append(tempString)
                text = text[0:i-1]
            if count == 3:
                tempList.append(text[0:i-1])
                i = 0
            else:
                i = i - 1
    if tempList[0].isnumeric() and tempList[1].isnumeric() and tempList[2].isnumeric():
        t = (int(tempList[2]), int(tempList[1]), int(tempList[0]), tempList[3])
    return t

def get_line(fname, parno, lineno):
    f = open(fname, "r")
    file = f.read()
    paras = file.split('\n\n')
    paras = [i for i in paras if i != '']
    para = paras[parno - 1].split('\n')
    line = para[lineno - 1]
    return line


totallines = ""

fileNum = (input("Please enter the file number ==> ")) + ".txt"
paraNum = int(input("Please enter the paragraph number ==> "))
lineNum = int(input("Please enter the line number ==> "))


line = parse_line((get_line(fileNum, paraNum, lineNum)))
print(line)
while line[3] != "END":
    totallines += line[3] + "\n"
    newline = parse_line(get_line(str(line[0]) + ".txt", line[1], line[2]))
    print(newline)
    line = newline

f = open("program.py", "w")
f.write(totallines)
# f.close()