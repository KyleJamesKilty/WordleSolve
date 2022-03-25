# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:27:41 2022

@author: Kyle
"""

def filterguess(PG,count,Correct,Present):
    for word,value in PG.items():
        if value == 0:
            continue
        for idx,letter in Correct.items(): #Correct letters in right spot
            if word[idx] != letter:
                PG[word] = 0
                break
        for idx,letter in Present.items(): #Present letters in wrong spot
            if word[idx] == letter:
                PG[word] = 0
                break
        for letter,amount in count.items(): #Handles letters 100% absent
            if amount[1] == 0:
                for let in word:
                    if letter == let:
                        PG[word] = 0
            else:
                counter = 0
                for let in word:
                    if let == letter:
                        counter += 1
                if counter >= amount[0] and counter <= amount[1]:
                    continue
                else:
                    PG[word] = 0
    return PG