# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:18:41 2020

@author: Goutam Dadhich
"""

# Program to find th factorial of the given number.

def Factorial_rec(num):
    if num == 0:
        return 1
    return num * Factorial_rec(num-1)

def Factorial_dp(num):
    Fac_Table = [1]
    
    for i in range(1, num+1):
        Fac_Table.append(i * Fac_Table[i-1])      
        
    return Fac_Table[num]

def Factorial_dp_advance(num):
    res = 1
    if num == 0:
        return res
    for i in range(1, num+1):
        res *= i
        
    return res

if __name__ == '__main__':
    num = 5
    print('-'*10 + '*'*5 + '-'*10)
    print('Using recurssion :- ')
    print('Factorial is :- ', Factorial_rec(num))
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Dynamic  programming :- ')
    print('Factorial is :- ', Factorial_dp(num))
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Dynamic  programming advance:- ')
    print('Factorial is :- ', Factorial_dp_advance(num))
    print('-'*10 + '*'*5 + '-'*10)