import sys

input = sys.stdin.readline

n = int(input())
period = 15 * 10 ** 5

dp = [1] * period
dp[0] = 0

for i in range(2, period):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
    
print(dp[n%period])