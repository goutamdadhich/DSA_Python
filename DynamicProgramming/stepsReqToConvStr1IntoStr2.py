# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:38:52 2020

@author: Goutam Dadhich
"""


def minChanges(X, Y, m, n):
    T = [[0 for i in range(n+1)] for j in range(m+1)]
    
    
    for i in range(n+1):
        T[0][i] = i
        
    for i in range(m+1):
        T[i][0] = i
    
    cost = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                cost = 0
            else:
                cost = 1
                
            T[i][j] = min(min(T[i-1][j]+1, T[i][j-1]+1), T[i-1][j-1]+cost)
    
    '''
    for i in T:
        print(i)
    '''
    return T[m][n]

if __name__ == '__main__':
    s1 = 'kitten'
    s2 = 'sitting'
    #s1 = 'ours'
    #s2 = 'hours'
    
    m = len(s1)
    n = len(s2)
    
    print(minChanges(s1, s2, m, n))