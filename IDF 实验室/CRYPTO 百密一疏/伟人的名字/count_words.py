#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 数单词数的
"""
def getWords():
    filename = "common_English_Word_Dictionary.txt"
    with open(filename, "r") as f:
        data = f.read()
        data = data.split("\n")
        data = set(data)

    return data

def countWords(words, string):
    count_words = 0
    for each in words:
        if len(each) < 2:
            continue
        position = findSubStr(each, string)
        count_words += len(position)

    return count_words

def findSubStr(subString,fullString):
    subString = subString.upper()
    fullString = fullString.upper()
    indexs = []
    fullLength = len(fullString)
    subLength = len(subString)
    for i in range(fullLength-subLength):
        if fullString[i:i+subLength] == subString:
            indexs.append(i)
    return indexs

def createMi_yao(order):
    character = "abcdefghijklmnopqrstuvwxyz"
    mi_yao = ""
    while order > 0:
        mi_yao += character[order % 26]
        order = order // 26
    return mi_yao

if __name__ == '__main__':
    words = getWords()
    string = """\
IN YOUR HANDS, MY FELLOW CITIZENS, MORE THAN IN MINE, WILL REST THE FINAL SUCCESS OR FAILURE OF OUR COURSE. SINCE THIS COUNTRY WAS FOUNDED, EACH GENERATION OF AMERICANS HAS BEEN SUMMONED TO GIVE TESTIMONY TO ITS NATIONAL LOYALTY. THE GRAVES OF YOUNG AMERICANS WHO ANSWERED THE CALL TO SERVICE SURROUND THE GLOBE. \
"""
#    for i in range(0,26 ** 5):
#        count_words = countWords(words, string)
#        if count_words > 20:
#        mi_yao = createMi_yao(i)
#        if mi_yao == "woldy":
#            print(mi_yao)
#            break
