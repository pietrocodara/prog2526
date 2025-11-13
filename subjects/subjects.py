#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys
from itertools import combinations
# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

N, M = map(int, input().strip().split())

K = [0 for i in range(N)]
S = [[] for i in range(N)]
for j in range(N):
    S[j] = list(map(int, input().strip().split()))
    K[j], S[j] = S[j][0], S[j][1:]

P = 0
pairs = [[1 for j in range(i)] for i in range(M)]
cont = M * (M - 1) // 2
for scelta in S:
    lung = len(scelta)
    if lung >= 2:
        scelta = sorted(scelta, reverse=True)
        for i in range(len(scelta)-1):
            for j in range(i+1, len(scelta)):
                a = scelta[i] - 1
                b = scelta[j] - 1
                if pairs[a][b] == 1:
                    pairs[a][b] = 0
                    cont -= 1

print(cont)
for i in range(M):
    for j in range(i):
        if pairs[i][j] == 1:
            print(i+1, j+1)

sys.stdout.close()
