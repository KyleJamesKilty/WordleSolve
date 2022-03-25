# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:32:01 2022

@author: Kyle
"""

from ThisIsTheOne import driver

def Tbd0():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[0].shadowRoot.querySelectorAll('game-tile')[0].shadowRoot")
def Tbd1():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[1].shadowRoot.querySelectorAll('game-tile')[0].shadowRoot")   
def Tbd2():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[2].shadowRoot.querySelectorAll('game-tile')[0].shadowRoot")
def Tbd3():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[3].shadowRoot.querySelectorAll('game-tile')[0].shadowRoot")
def Tbd4():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[4].shadowRoot.querySelectorAll('game-tile')[0].shadowRoot")
def Tbd5():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[5].shadowRoot.querySelectorAll('game-tile')[0].shadowRoot")