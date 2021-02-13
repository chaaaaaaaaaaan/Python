# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:09:20 2021

@author: skukm
"""

keypad=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

def lotation(h):
    for i in range(4):
        for j in range(3):
            if h==keypad[i][j]: l=[i,j]
    return l
            
            
def solution(numbers,hand):
    left=[3,0]
    right=[3,2]
    answer=''    
    for i in range(len(numbers)):
        print(left, right, numbers[i])
        if numbers[i] in [1,4,7]:
            answer+='L'
            left=lotation(numbers[i])
        elif numbers[i] in [3,6,9]:
            answer+='R'
            right=lotation(numbers[i])
        else: 
            l_d=0
            r_d=0
            for d in range(2):
                l_d+=abs(lotation(numbers[i])[d]-left[d])
                r_d+=abs(lotation(numbers[i])[d]-right[d])                
            #print(l_d,r_d)
            if l_d<r_d: 
                answer+='L'
                left=lotation(numbers[i])
            elif l_d>r_d: 
                answer+='R'
                right=lotation(numbers[i])
            else: 
                if hand=="left": 
                    answer+='L'
                    left=lotation(numbers[i])
                if hand=="right": 
                    answer+='R'
                    right=lotation(numbers[i])
    return answer

