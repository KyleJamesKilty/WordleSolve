# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 07:14:47 2022


@author: Kyle
"""
from Wordle import data

dicOne = {}
dicTwo = {}
Three = []
notDone = 1

while notDone:
    finalList = []
    corPos = 1
    cor = 1
    FalseLet = 1
    
    while corPos:
        corPos = input('Letter in Correct Position: ')
        corPos = corPos.lower()
        if corPos == '0':
            break
        if corPos:
            Pos = input('Position Index: ')
            dicOne[corPos] = int(Pos)
    while cor:
        cor = input('Letter in Incorrect Postiion: ')
        cor = cor.lower()
        if cor == '0':
            break
        if cor:
            IncPos = input('Position Index: ')
            IncPos = int(IncPos)
            if IncPos not in dicOne:
                if IncPos not in dicTwo:
                    dicTwo[cor] = [IncPos]
                else:
                    dicTwo[cor].append(IncPos)           
    while FalseLet:
        FalseL = input('Letter not in Word: ')
        FalseL = FalseL.lower()
        if FalseL == '0':
            break
        if FalseL not in dicOne or FalseL not in dicTwo and FalseL not in Three:
            Three.append(FalseL)
        
    for word,value in data.items():
        count = 0
        if value == 0:
            continue
        for letter,pos in dicOne.items():
            if word[pos] != letter:
                data[word] = 0
                break
        for letter,poses in dicTwo.items():
            for pos in poses:
                if word[pos] == letter:
                    data[word] = 0
                    break
        for letter in word:
            if letter in Three:
                data[word] = 0
                break
            if letter in dicTwo:
                count += 1
        if count < len(dicTwo):
            data[word] = 0
        else:
            if data[word] == 1:
                finalList.append(word)
    print(finalList)