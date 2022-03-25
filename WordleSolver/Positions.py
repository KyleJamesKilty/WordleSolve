# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:10:31 2022

@author: Kyle
"""
Correct = {}
Present = {}

def position(evalu,letter,idx):
    if evalu == "correct":
        Correct[idx] = letter
    elif evalu == "present":
        if idx in Present:
            Present[idx].append(letter)
        else:
            Present[idx] = [letter]
    
        
        