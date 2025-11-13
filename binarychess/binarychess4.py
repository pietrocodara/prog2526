#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input1.txt')
# sys.stdout = open('output.txt', 'w')

R, C, N = map(int, input().strip().split())
nodes=[]
for i in range(N):
    nodes.append(tuple(map(int, input().strip().split())))
K=0

n = len(nodes)

# Mappe per collegamenti rapidi
rows = {}
cols = {}
diag1 = {}
diag2 = {}
for i, (r, c) in enumerate(nodes):
    rows.setdefault(r, []).append(i)
    cols.setdefault(c, []).append(i)
    diag1.setdefault(r - c, []).append(i)
    diag2.setdefault(r + c, []).append(i)

visited = [False] * n
components = []

for i in range(n):
    if visited[i]:
        continue
    stack = [i]
    comp = []
    while stack:
        curr = stack.pop()
        if visited[curr]:
            continue
        visited[curr] = True
        comp.append(nodes[curr])
        r, c = nodes[curr]
        neighbors = set(rows[r] + cols[c] + diag1[r - c] + diag2[r + c])
        for nei in neighbors:
            if not visited[nei]:
                stack.append(nei)
    components.append(comp)

K = len(components)
print(pow(2, K, 10**9 + 7))

sys.stdout.close()
