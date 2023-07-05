import sys

n = int(input())
data = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0

for i in range(n):
    result += 1
    data[i] -= b

    if data[i] > 0:
        if data[i] % c == 0:
            result += data[i] // c
        else:
            result += data[i] // c + 1

print(result)
