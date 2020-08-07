# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:41:51 2020

@author: Goutam Dadhich
"""

# 0 1 1 2 3 5 8 13 21
def Fib_rec(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return Fib_rec(num-1) + Fib_rec(num-2)

def Fib_dp(num):
    fib_table = [0, 1]
    
    for i in range(2, num+1):
        fib_table.append(fib_table[i-1]+ fib_table[i-2])
        
    return fib_table[num-1]

def Fib_dp_advance(num):
    a, b = 0, 1
    
    for i in range(2, num+1):
        a, b = b, a+b
        
    return a

if __name__ == '__main__':
    num = 6
    print('-'*10 + '*'*5 + '-'*10)
    print('Using recurssion :- ')
    print('Fibonaci term is :- ', Fib_rec(num))
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Dynamic  programming :- ')
    print('Fibonaci term is :- ', Fib_dp(num))
    print('-'*10 + '*'*5 + '-'*10)
    print('Using Dynamic  programming advance:- ')
    print('Fibonaci term is :- ', Fib_dp_advance(num))
    print('-'*10 + '*'*5 + '-'*10)