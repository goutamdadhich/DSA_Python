# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:16:59 2020

@author: Goutam Dadhich
"""

"""
LCS Problem -> Printing Length 
"""

d = {}

def Lcs_rec(X, Y, m, n):
    if m == 0 or n==0:
        return 0
    
    if X[m-1] == Y[n-1]:
        return 1 + Lcs_rec(X, Y, m-1, n-1)
    return max(Lcs_rec(X, Y, m-1, n), Lcs_rec(X, Y, m, n-1))

               
def Lcs_rec_dp(X, Y, m, n):
    if m ==0 or n==0:
        return 0
    
    key = str(m)+'-'+str(n)
    
    if key not in d:
        if X[m-1] == Y[n-1]:
            d[key] = 1 + Lcs_rec_dp(X, Y, m-1, n-1)
        else:
            d[key] = max(Lcs_rec_dp(X, Y, m-1, n), Lcs_rec_dp(X, Y, m, n-1))    
    return d[key]

def Lcs_dp(X, Y, m, n):
    T = [[0 for i in range(n+1)] for j in range(m+1)] # [[0]*(n+1)]*(m+1) 
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    #print(T)
    return T[m][n]

if  __name__ == '__main__':
    X="ABCBDAB"
    Y="BDCABA"
    print('-'*10+'*'*5+'-'*10)
    print('Using recurssion:- ')
    print('Length of lcs :- ',Lcs_rec(X, Y, len(X), len(Y)))
    print('-'*10+'*'*5+'-'*10)
    print('Using recurssion with dp:- ')
    print('Length of lcs :- ',Lcs_rec_dp(X, Y, len(X), len(Y)))
    print('-'*10+'*'*5+'-'*10)
    print('Using dp(string  pattern matching algorithm):- ')
    print('Length of lcs :- ',Lcs_dp(X, Y, len(X), len(Y)))
    print('-'*10+'*'*5+'-'*10)
    