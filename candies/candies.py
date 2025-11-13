#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.


# input data
N = int(input().strip())
S = list(map(int, input().strip().split()))


# insert your code here

S.sort()
min_candies = 1
num = 1
for i in range(1,N):
    if S[i]>S[i-1]:
        num += 1
    min_candies += num
print(min_candies)