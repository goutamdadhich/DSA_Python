# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 18:34:17 2020

@author: Goutam Dadhich
"""

"""
Rod Cut Problem
"""

import sys

INT_MIN = -sys.maxsize


def RodCut_rec(length, price, rod):
    if rod == 0:
        return 0
    
    profit = INT_MIN
    
    for i in range(1, rod+1):
        res = price[i-1] + RodCut_rec(length, price, rod-i )
        
        if res > profit:
            profit = res
            
    return profit


def RodCut_dp(length, price, rod):
    T = [0]*(rod+1)
    T[0] = 0
    
    for i in range(1, rod+1):
        res = INT_MIN
        
        for j in range(0, i):
            res = max(res, price[j] + T[i-j-1])
            
        T[i] = res
        
    return T[rod]
        

if __name__ == "__main__":
    length = [1,2,3,4,5,6,7,8,9]
    price = [1,5,8,9,10,17,17,20,22]
    rod = 4
    
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Recurssion:- ')
    print('Maximum profit :- ', RodCut_rec(length, price, rod))
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Recurssion:- ')
    print('Maximum profit :- ', RodCut_dp(length, price, rod))
    print('-'*10 + '*'*5 + '-'*10)