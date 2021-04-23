# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:46:56 2020

@author: Goutam Dadhich
"""

D, P = map(int, input().split())

hp = D//P

def SieveOfEratosthenes(n): 
    global d
    d = {} 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n+1): 
        if prime[p]: 
            d[p] = True
        else:
            d[p] = False
    #return d

SieveOfEratosthenes(D)
n = hp
res = 0
while n>1:
    i = 1
    counter = 0
    while True:
        j = (i-1)*hp + n
        
        if d[j] and j<=D:
            counter += 1
        else:
            break
        if i == P:
            break
        i += 1
    if counter == P:
        res += 1
    n -= 1
    
print(res)
            
        



    