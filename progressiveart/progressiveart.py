#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

N, M, L, K = map(int, input().strip().split())

# INSERT YOUR CODE HERE

max_squares = max(0, N-L+1) * max(0, M-L+1)
if K == 0:
    print("YES")
    for i in range(N):
        print('R'*M)
elif L%3 == 0 and K <= max_squares: # fattibile, posso piazzare i quadrati
    print("YES")
    colors = ['R', 'G', 'B']
    index = 0
    A = [[colors[(i+j)%3] for i in range(L)] for j in range(L)]
    beautiful = 1
    # costruisco fino a LxM
    for x in range(M - L):
        beautiful += 1
        for y in range(L):
            new_color = 'R' if beautiful > K else A[y][x % L]
            A[y].append(new_color)
    
    # N-L righe rimanenti (da riempire in qualche modo)
    # M-L+1 quadrati possibili per riga
    if beautiful < K:
        full_rows = (K - beautiful) // (M - L + 1)
        extra_squares = (K - beautiful) % (M - L + 1)
        new_car = 'R'
        for x in range(full_rows):
            A.append(A[x % L])
            beautiful += (M - L + 1)    
        if extra_squares > 0:
            A.append(A[full_rows % L][:])
            new_car = 'R' if A[-1-L][M - extra_squares] != 'R' else 'G'
            for x in range(M - extra_squares, M):
                A[-1][x] = new_car
                beautiful += 1
    if len(A) < N:
        new_row = ['R' for _ in range(M)]
        for x in range(N - len(A)):
            A.append(new_row)

    A = [''.join(row) for row in A]
    for row in A:
        print(row)
else:
    print("NO")

sys.stdout.close()
