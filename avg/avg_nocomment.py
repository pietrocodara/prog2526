#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys
N, K = map(int, input().strip().split())
P = list(map(int, input().strip().split()))

somma_target = N*K
somma_P = sum(P)
diff = somma_target - somma_P
index = 0 

if diff > 0:
    index = 1
elif diff < 0:
    P.sort(reverse=True)
    while (diff < 0 and index < N):
        diff += P[index] - 1
        index += 1
    
print(index)
sys.stdout.close()
