# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:32:41 2020

@author: Goutam Dadhich
"""

"""
Given the mobile numeric keypad. You can only press buttons that are 
up, left, right or down to the current button. You are not allowed to 
press bottom row corner buttons (i.e. * and # ).

Given a number N, find out the number of possible numbers of given length


Examples:
For N=1, number of possible numbers would be 10 (0, 1, 2, 3, …., 9)
For N=2, number of possible numbers would be 36
Possible numbers: 00,08 11,12,14 22,21,23,25 and so on.

"""
def isValid(i, j):
    if i==3 and (j==0 or j==2):
        return 0
    
    return (i<=3 and i>=0 and j>=0 and j<=3)


def keyPairs_rec(N):
    if N==0:
        return 0
    
    
    
    

def keyPairs_dp(N):
    pass


if  __name__ == '__main__':
    N = 2
    global Keypad
    Keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              ['*', 0, '#']]
    
    print('-'*10+'*'*5+'-'*10)
    print('Using recurssion:- ')
    print('Possible Numbers :- ',keyPairs_rec(N))
    print('-'*10+'*'*5+'-'*10)
    print('Using dp:- ')
    print('Possible Numbers :- ',keyPairs_dp(N))
    print('-'*10+'*'*5+'-'*10)