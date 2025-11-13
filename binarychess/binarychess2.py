#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input1.txt')
# sys.stdout = open('output.txt', 'w')

R, C, N = map(int, input().strip().split())

rr = [0 for i in range(N)]
cc = [0 for i in range(N)]
nodes = []
for i in range(N):
    r,c = map(int, input().strip().split())
    nodes.append((r,c))
K=0

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

visited = [False] * N

def dfs(i, component):
    if visited[i]:
        return
    visited[i] = True
    component.append(nodes[i])
    
    r, c = nodes[i]
    neighbors = set(rows[r] + cols[c] + diag1[r - c] + diag2[r + c])
    for j in neighbors:
        dfs(j, component)

components = []
for i in range(N):
    if not visited[i]:
        comp = []
        dfs(i, comp)
        components.append(comp)

K = len(components)
print(pow(2, K, 10**9 + 7))

sys.stdout.close()
