import sys

input = sys.stdin.readline

n = int(input())

datas = list(map(int, input().split()))

d = [1] * n

for i in range(0, n):
    for j in range(i+1, n):
        if datas[j] < datas[i]:
            d[j] = -min(-d[j], -(d[i] + 1))

result = n - max(d)

print(result)
