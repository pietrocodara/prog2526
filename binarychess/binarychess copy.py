#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input1.txt')
# sys.stdout = open('output.txt', 'w')

R, C, N = map(int, input().strip().split())




rr = [0 for i in range(N)]
cc = [0 for i in range(N)]

for i in range(N):
    rr[i], cc[i] = map(int, input().strip().split())
K=0
while rr:
    conn_riga = set()
    conn_colonna = set()
    conn_somma = set()
    conn_diff = set()
    
    r = rr.pop()
    c = cc.pop()
    s = r + c
    d = r - c
    # trova tutti gli indici degli elementi sulla stessa riga
    indici_riga = [i for i, el in enumerate(rr) if el == r]
    # degli elementi sulla stessa riga memorizzo i valori di colonna, somma e differenza
    for i in sorted(indici_riga, reverse=True):
        conn_colonna.add(cc[i])
        conn_somma.add(rr[i]+cc[i])
        conn_diff.add(rr[i]-cc[i])
        del rr[i]
        del cc[i]
    
    # trova tutti gli indici degli elementi sulla stessa colonna
    indici_colonna = [i for i, el in enumerate(cc) if el == c]
    # degli elementi sulla stessa memorizzo i valori di riga, somma e differenza
    for i in sorted(indici_colonna, reverse=True):
        conn_riga.add(rr[i])
        conn_somma.add(rr[i]+cc[i])
        conn_diff.add(rr[i]-cc[i])
        del rr[i]
        del cc[i]
    
    # trova tutti gli indici degli elementi sulla stessa diagonale per somma
    indici_somma = [i for i, el in enumerate([x + y for x, y in zip(rr, cc)]) if el == s]
    # degli elementi connessi al primo per somma, memorizzo i valori di riga, colonna e differenza
    for i in sorted(indici_somma, reverse=True):
        conn_riga.add(rr[i])
        conn_colonna.add(cc[i])
        conn_diff.add(rr[i]-cc[i])
        del rr[i]
        del cc[i]
    
    # trova tutti gli indici degli elementi sulla stessa diagonale per differenza
    indici_diff = [i for i, el in enumerate([x - y for x, y in zip(rr, cc)]) if el == d]
    # degli elementi connessi al primo per differenza, memorizzo i valori di riga, colonna e somma
    for i in sorted(indici_diff, reverse=True):
        conn_riga.add(rr[i])
        conn_colonna.add(cc[i])
        conn_somma.add(rr[i]+cc[i])
        del rr[i]
        del cc[i]
    
    # finché ci sono elementi in crique, esaminiamoli uno ad uno
    while conn_riga or conn_colonna or conn_somma or conn_diff:
        if conn_riga:
            # trova tutti gli indici degli elementi sulla stessa riga
            indici_riga = [i for i, el in enumerate(rr) if el in conn_riga]
            # degli elementi sulla stessa riga memorizzo i valori di colonna, somma e differenza
            for i in sorted(indici_riga, reverse=True):
                conn_colonna.add(cc[i])
                conn_somma.add(rr[i]+cc[i])
                conn_diff.add(rr[i]-cc[i])
                del rr[i]
                del cc[i]
            conn_riga.clear()
        
        if conn_colonna:
            # trova tutti gli indici degli elementi sulla stessa colonna
            indici_colonna = [i for i, el in enumerate(cc) if el in conn_colonna]
            # degli elementi sulla stessa memorizzo i valori di riga, somma e differenza
            for i in sorted(indici_colonna, reverse=True):
                conn_riga.add(rr[i])
                conn_somma.add(rr[i]+cc[i])
                conn_diff.add(rr[i]-cc[i])
                del rr[i]
                del cc[i]
            conn_colonna.clear()
        
        if conn_somma:
            # trova tutti gli indici degli elementi sulla stessa diagonale per somma
            indici_somma = [i for i, el in enumerate([x + y for x, y in zip(rr, cc)]) if el in conn_somma]
            # degli elementi connessi al primo per somma, memorizzo i valori di riga, colonna e differenza
            for i in sorted(indici_somma, reverse=True):
                conn_riga.add(rr[i])
                conn_colonna.add(cc[i])
                conn_diff.add(rr[i]-cc[i])
                del rr[i]
                del cc[i]
            conn_somma.clear()

        if conn_diff:
            # trova tutti gli indici degli elementi sulla stessa diagonale per differenza
            indici_diff = [i for i, el in enumerate([x - y for x, y in zip(rr, cc)]) if el in conn_diff]
            # degli elementi connessi al primo per differenza, memorizzo i valori di riga, colonna e somma
            for i in sorted(indici_diff, reverse=True):
                conn_riga.add(rr[i])
                conn_colonna.add(cc[i])
                conn_somma.add(rr[i]+cc[i])
                del rr[i]
                del cc[i]
            conn_diff.clear()
        
    K += 1
    K = K % (10**9 + 7)
    # print(K, rr, cc)

print(pow(2, K, 10**9 + 7))

sys.stdout.close()
