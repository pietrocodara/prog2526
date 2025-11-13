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

    conn_riga.add(r)
    conn_colonna.add(c)
    conn_somma.add(r + c)
    conn_diff.add(r - c)
    # elimino elemento se connesso a uno dei precedenti
    lun = len(rr)
    for i in range(lun-1,-1,-1):
        if rr[i] in conn_riga or cc[i] in conn_colonna or (rr[i]+cc[i]) in conn_somma or (rr[i]-cc[i]) in conn_diff:
            # aggiorno gli insiemi
            conn_riga.add(rr[i])
            conn_colonna.add(cc[i])
            conn_somma.add(rr[i]+cc[i])
            conn_diff.add(rr[i]-cc[i])
            # elimino l'elemento
            del rr[i]
            del cc[i]
        else:
            # qui dovrei formare l'altro insieme di connessione
            # conn_riga eccetera dovrebbero essere array e il controllo di questo if un ciclo
            pass
        
    K += 1
    # K = K % (10**9 + 7)
    # print(K, rr, cc)

print(pow(2, K, 10**9 + 7))

sys.stdout.close()
