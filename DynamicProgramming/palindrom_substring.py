# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 08:35:04 2020

@author: Goutam Dadhich
"""


def longestPalindrome(s: str) -> str:
    n=len(s)
    if n<=1:
        return s
    T=[[0]*(n) for i in range(n)]
    for i in range(n):
        T[i][i]=1
    
    res = s[0]
    k=1
    l=1
    for j in range(1,n):
        for i in range(n-j):
            if (s[i]==s[j+i]) and ((j==1) or (T[i+1][j+i-1]==1)):
                T[i][j+i]=1
                k=i
                l=j+i
            else:
                T[i][j+i]=0
    if (l-k>=1):
        res = s[k:l+1]
        
    '''for i in T:
        print(i)
        '''
    
    return res


st = 'aabbaaaa'
print(longestPalindrome(st))