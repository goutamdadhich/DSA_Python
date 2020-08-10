# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:35:04 2020

@author: Goutam Dadhich
"""

def lcsubstring(X, Y, m,n):
    T = [[0 for i in range(n+1)] for j in range(m+1)]
    
    maxlen = 0
    endindex = m
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
                if T[i][j] > maxlen:
                    maxlen = T[i][j]
                    endindex = i
                    
    return X[endindex-maxlen : maxlen]

X = 'BABA'
Y = 'ABAB'
m = len(X)
n = len(Y)
print('-'*10+'*'*5+'-'*10)
print('Using Dynamic Programming :- ')
print('Longest common sub-String :- ', lcsubstring(X, Y, m, n))
print('-'*10+'*'*5+'-'*10)