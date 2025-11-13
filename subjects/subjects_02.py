#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys
from itertools import combinations
from itertools import chain
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
# ans = [[0 for j in range(2)] for i in range(1000000)]
pairs = set(map(frozenset,combinations(range(1,M+1),2)))

for scelta in S:
    courses = set(chain.from_iterable(pairs))
    scelta = set(scelta)
    scelta = scelta.intersection(courses)
    if len(scelta) < 2:
        continue
    pairs -= set(map(frozenset,combinations(scelta,2)))

P = len(pairs)
print(P)
for pair in pairs:
    print(*pair)

sys.stdout.close()
