#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

T = int(input().strip())
for _ in range(T):

    # input data
    N, Q = map(int, input().strip().split())
    P = list(map(int, input().strip().split()))
    T = list(map(int, input().strip().split()))


    # insert your code here
    hacker = False
    progressivo = 0
    for t in T:
        if t < 0:
            progressivo -= P[-t-1]
        else:
            progressivo += t
        if progressivo < 0:
            hacker = True
            break
    # print the result
    if hacker:
        print('HACKER')
    else:
        print('OK')
