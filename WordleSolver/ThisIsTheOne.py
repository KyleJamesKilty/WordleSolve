# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 23:55:07 2022

@author: Kyle
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from Counter import Count,PreCount,count
from Positions import position,Correct,Present
from Wordle import data
from FilteringLogic import filterguess
import random


def getattributes(item):
    item = item.find_elements(By.TAG_NAME, "game-tile" )
    totalAbsent = 0
    for i in item:
        evalu = i.get_attribute("evaluation")
        if evalu == "absent":
            totalAbsent += 1
    for idx,i in enumerate(item):
        evalu = i.get_attribute("evaluation")
        letter = i.get_attribute("letter")
        PreCount(evalu,letter,idx,preCount)
        position(evalu,letter,idx)
    count = Count(totalAbsent,preCount)
    
    
def Output0():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[0].shadowRoot")
def Output1():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[1].shadowRoot")   
def Output2():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[2].shadowRoot")
def Output3():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[3].shadowRoot")
def Output4():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[4].shadowRoot")
def Output5():
    return driver.execute_script("return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[5].shadowRoot")
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

def preparepage():
    actions = ActionChains(driver)
    actions.click()
    actions.pause(2)
    actions.move_by_offset(500, 900)
    actions.perform()

def sendguess(guess,pause):
    actions = ActionChains(driver)
    actions.send_keys(guess)
    actions.send_keys(Keys.RETURN)
    actions.pause(pause)
    actions.perform()
    
def delete():
    actions = ActionChains(driver)
    for j in range(5):
        actions.send_keys(Keys.BACK_SPACE)
    actions.perform()
    
def refresh():
    item0 = Output0()
    item1 = Output1()
    item2 = Output2()
    item3 = Output3()
    item4 = Output4()
    item5 = Output5()
    return [item0,item1,item2,item3,item4,item5]

def refreshTbd():
    tb0 = Tbd0()
    tb1 = Tbd1()
    tb2 = Tbd2()
    tb3 = Tbd3()
    tb4 = Tbd4()
    tb5 = Tbd5()
    return [tb0,tb1,tb2,tb3,tb4,tb5]

def randomWord():
    guess = random.randint(0,10000)
    for idx,key in enumerate(data.keys()):
        if idx == guess:
            break
    return key
    
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.nytimes.com/games/wordle/index.html")

preparepage()
sendguess("sluts", 2)
notSolved = True
while notSolved:
    for i in range(5):
        list_ = refresh()
        preCount = {}
        getattributes(list_[i])
        data = filterguess(data,count,Correct,Present)
        print('here')
        for key,value in data.items():
            if value == 1:
                print(key)
                sendguess(key,2)
                Tbdlist = refreshTbd()
                Check = Tbdlist[i+1].find_element(By.CLASS_NAME,"tile")
                isAbsent = (Check.get_attribute("data-state"))
                print(isAbsent)
                if isAbsent == "tbd" :
                    delete()
                    data[key] = 0
                    continue
                else:
                    data[key] = 0
                    break
        
        
    
        
        
        




        








    







