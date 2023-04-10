import sys

input = sys.stdin.readline

n = int(input())
A = [0] * 26
result = 0

for _ in range(n):
    data = input().rstrip()
    for j in range(len(data)):
        A[ord(data[j]) - ord("A")] += 10 ** (len(data) -1 - j)

A.sort(reverse = True)
n = 9

for j in range(len(A)):
    if n == 0: break
    result += A[j] * n
    n -= 1 

print(result)