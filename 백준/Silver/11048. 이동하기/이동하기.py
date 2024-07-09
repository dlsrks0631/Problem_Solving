import sys

input = sys.stdin.readline

# 3, 4
N,M = map(int,input().split())
dp = []

for _ in range(N):
    dp.append(list(map(int,input().split())))

# 초기값 세팅
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + dp[i][0]

for j in range(1, M):
    dp[0][j] = dp[0][j-1] + dp[0][j]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + dp[i][j]

print(dp[N-1][M-1])