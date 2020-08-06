# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 18:29:13 2020

@author: Goutam Dadhich
"""

import sys

INT_MAX = sys.maxsize
# print(INT_MAX)

# Finding Minimum Coins using Recursio
def FindMinCoins_rec(coins, n, amt):
    if amt == 0:
        return 0
    
    if amt < 0:
        return INT_MAX
    
    count = INT_MAX
    
    for i in range(0, n):
        res = FindMinCoins_rec(coins, n, amt-coins[i])
        
        if res != INT_MAX:
            count = min(res+1, count)
            
    return count

# Finding Minimum Coins using Dynamic programming
def FindMinCoins_dp(coins, n, amt):
    T = [INT_MAX]*(amt+1)
    
    T[0] = 0
    
    for i in range(1, amt+1):
        res = INT_MAX
        
        for j in range(0, n):
            if i-coins[j] >= 0:
                res = T[i - coins[j]]
                
            if res != INT_MAX:
                T[i] = min(res+1, T[i])
                
    return T[amt]


if __name__ == '__main__':
    coins = [1, 2, 3, 5, 7]
    n = len(coins)
    amt = 15

    print('-'*10 + '*'*5 + '-'*10)
    print('Using Recurssion:- ')
    print('Minimum coins required :- ', FindMinCoins_rec(coins, n, amt))
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Recurssion:- ')
    print('Minimum coins required :- ', FindMinCoins_dp(coins, n, amt))
    print('-'*10 + '*'*5 + '-'*10)
    