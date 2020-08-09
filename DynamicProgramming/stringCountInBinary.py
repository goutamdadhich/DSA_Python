# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:07:31 2020
@author: Goutam Dadhich
"""

"""
Statement :- you are given a integer n  and your task is to return number 
of binary patterns that don't have 2 continue 1's in it.

"""

def stringCount_rec(n, last_digit):
    pass

def stringCount_dp(n):
    T = [[0 for i in range(2)] for i in range(n+1)]
    T[0][0] = 0
    T[0][1] = 0
    
    T[1][0] = 2
    T[1][1] = 1
    
    for i in range(2, n+1):
        T[i][0] = T[i-1][0] + T[i-1][1]
        T[i][1] = T[i-1][0]
        
    #print(T)    
    return T[n][0]

if __name__ == '__main__':
    n = 3
    print('-'*10 + '*'*5 + '-'*10)
    print('Using recurssion :- ')
    print('Number of term is :- ', stringCount_rec(n, 0))
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Dynamic  programming :- ')
    print('Number of term is :- ', stringCount_dp(n))
    print('-'*10 + '*'*5 + '-'*10)
    