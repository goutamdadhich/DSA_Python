# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:49:10 2020

@author: Goutam Dadhich
"""

n = int(input())

arr = [0]*3

print(arr)

for i in range(3):
    arr[i] = list(input())
    
"""
*.*#***#***#***.*.
*.*#*.*#.*.#******
***#***#***#****.*
"""
for i in arr:
    print(i)
    
out = ''


j =0
while j <n:
    if arr[0][j]=='*' and arr[1][j]=='*' and arr[2][j]=='*':
        if arr[0][j+1]=='.' and arr[1][j+1]=='.' :
            out += 'U'
            j += 3
            continue
        
            
        elif arr[0][j+1]=='*' and arr[1][j+1]=='*' and arr[2][j+1]=='*':
            out += 'E'
            j += 3
            continue
                
        else:
            out += 'O'
            j += 3
            continue
                
                
    elif arr[0][j]=='.' and arr[1][j]=='*':
        out += 'A'
        j += 3
        continue
        
        
    elif arr[0][j]=='*' and arr[1][j]=='.':
        out += 'I'
        j += 3
        continue
        
        
    if arr[0][j] == '#':
        out += '#'
        j += 1
        continue
        
    
print(out)
    