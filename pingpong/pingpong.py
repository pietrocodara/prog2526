#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys
# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    A, B = map(int, input().strip().split())
    
    if A < 33: # impossibile per A vincere 3 set
        print(-1,-1)
    elif A == 33 and B <= 30: # A vince 3-0
        for _ in range(3):
            D = min(10,B)
            B -= D
            print(11,D)
    elif A <= 43 and B >= 11 and B <= 41: # A vince 3-1
        B-=11
        A-=33                
        for _ in range(2): # due set vinti da A
            D = min(10,B)
            B -= D
            print(11,D)
        print(A,11) # set vinto da B
        D = min(10,B)
        B -= D
        print(11,D) # set vinto da A
    elif A <= 53 and B >= 22 and B <= 52: # A vince 3-2
        B-=22
        A-=33                
        for _ in range(2): # due set vinti da A
            D = min(10,B)
            B -= D
            print(11,D)          
        for _ in range(2): # due set vinti da B
            C = min(10,A)
            A -= C
            print(C,11)
        D = min(10,B)
        B -= D
        print(11,D) # set vinto da A
    else:
        print(-1,-1)
            

sys.stdout.close()
