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

# Union-Find senza classi
parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[py] = px

# Mappe per collegamenti rapidi
rows = {}
cols = {}
diag1 = {}  # r - c
diag2 = {}  # r + c

for i, (r, c) in enumerate(nodes):
    for key, mp in [(r, rows), (c, cols), (r-c, diag1), (r+c, diag2)]:
        if key in mp:
            union(i, mp[key])
        mp[key] = i

# Raggruppa nodi per componente
components = {}
for i in range(n):
    root = find(i)
    components.setdefault(root, []).append(nodes[i])

K = len(components)
print(pow(2, K, 10**9 + 7))

sys.stdout.close()
