import sys

input = sys.stdin.readline

n, k = map(int, input().split())

datas = []
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    weight, value = map(int, input().split())
    datas.append((weight, value))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < datas[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(datas[i-1][1] + dp[i-1][j - datas[i-1][0]], dp[i-1][j])

print(dp[n][k])
