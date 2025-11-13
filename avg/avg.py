#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

N, K = map(int, input().strip().split())
P = list(map(int, input().strip().split()))

# INSERT YOUR CODE HERE
# Mi interessa arrivare a somma degli elementi di P uguale a N*K!!!
somma_target = N*K
somma_P = sum(P)
diff = somma_target - somma_P
index = 0 # usato cone indice per l'array, alla fine conterà il numero di elementi (prezzi) modificati

if diff > 0:
    index = 1 # mi basta sempre cambiare un elemento
    # Il codice seguente è errato: il testo non dice che il massimo prezzo è 1_000_000!
    # P.sort()
    # while (diff > 0 and index < N):
    #     # la differenza deve *diminuire* fino a 0
    #     # ovvero, la somma di P deve crescere per arrivare a somma_target
    #     # il massimo valore per ogni elemento di P è 1_000_000
    #     diff -= 1_000_000 - P[index] # L'elemento piu' piccolo cresce fino a 1_000_000
    #     index += 1
elif diff < 0:
    P.sort(reverse=True)
    while (diff < 0 and index < N):
        # la differenza deve *aumentare* fino a 0
        # ovvero, la somma di P deve diminuire per arrivare a somma_target
        # il minimo valore per ogni elemento di P è 1
        diff += P[index] - 1 # L'elemento piu' grande diminuisce fino a 1
        index += 1
    
print(index)
sys.stdout.close()
