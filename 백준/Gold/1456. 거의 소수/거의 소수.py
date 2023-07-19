import sys
import math

input = sys.stdin.readline

a,b = map(int,input().split())
A = [0] * (10**7 + 1)

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] == 0:
        continue
    for j in range(i * 2, len(A), i):
        A[j] = 0
        
result = 0

for i in range(2, 10**7 + 1):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= b / temp:
            if A[i] >= a / temp:
                result += 1
            temp *= A[i]
            
print(result)