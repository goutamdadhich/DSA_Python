# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:04:00 2020

@author: Goutam Dadhich
"""

"""

Given number is sum of any subSet's element of a given set or not.'

"""

def SumOfSub_rec(elems, n, num):
    if num == 0:
        return 1
    
    if n<=0 or num<0:
        return 0
    
    include = SumOfSub_rec(elems, n-1, num - elems[n-1])
    exclude = SumOfSub_rec(elems, n-1, num)
    
    return include or exclude
    
    

def SumOfSub_dp(elems, n, num):
    T = [([0]*(num+1))]*(n+1)
    
    for i in range(0, n+1):
        T[i][0] = 1
        
    for i in range(1, n+1):
        for j in range(1, num+1):
            if elems[i-1] > j :
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i][j - elems[i-1]]
                
    return T[n][num]


if __name__ == '__main__':
    elems = [7,3,5,8]
    num = 15
    n = len(elems)
    
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Recurssion:- ')
    print('Sum of any subset :- ', SumOfSub_rec(elems, n, num))
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Dynamic Programming:- ')
    print('Sum of any subset :- ', SumOfSub_dp(elems, n, num))
    print('-'*10 + '*'*5 + '-'*10)