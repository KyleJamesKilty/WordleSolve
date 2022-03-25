# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:35:31 2022

@author: Kyle
"""


count = {}

def PreCount(evalu,letter,idx,preCount):
    if letter not in preCount:
        preCount[letter] = [(evalu,idx)]
    else:
        preCount[letter].append((evalu,idx))

def Count(totalAbsent,preCount)  :
    for letter,value in preCount.items():
        countAbsent = 0
        countPresent = 0
        countCorrect = 0
        for v in value:
            if v[0] == "absent":
                countAbsent += 1
            if v[0] == "present":
                countPresent += 1
            if v[0] == "correct":
                countCorrect += 1
        count.pop(letter, None)
        if countAbsent == 0:
            count[letter] = (countPresent + countCorrect, totalAbsent + countPresent + countCorrect)
        else:
            if not countPresent and not countCorrect:
                count[letter] = (0,0)
            else:
                count[letter] = (countPresent + countCorrect,countPresent + countCorrect)
    return count
            
        
        




