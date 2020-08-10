# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:49:01 2020

@author: Goutam Dadhich
"""

def Lcs_dp(X, Y, m, n):
    global T 
    
    T =  [[0 for i in range(n+1)] for j in range(m+1)] 
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
                
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
            
    return T[m][n]

            
def Lcs_string(X, Y, m, n):
    if m == 0 or n == 0:
        return ''
    
    if X[m-1] == Y[n-1]:
        return Lcs_string(X, Y, m-1, n-1)+X[m-1]
    
    if T[m][n-1] > T[m-1][n]:
        return Lcs_string(X, Y, m, n-1)
    else:
        return Lcs_string(X, Y, m-1, n)
    
    
            

if __name__ == '__main__':
    X="ABCBDAB"
    Y="BDCABA"
    m = len(X)
    n = len(Y)
    print('-'*10+'*'*5+'-'*10)
    print('Using Dynamic Programming :- ')
    print('Length of lcs :- ',Lcs_dp(X, Y, m, n))
    print('String :- ', Lcs_string(X, Y, m, n))
    print('-'*10+'*'*5+'-'*10)
    