import sys
from collections import deque

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

data1 = list(input().rstrip())
data2 = list(input().rstrip())

dp = [[0] * (len(data2) + 1) for _ in range(len(data1) + 1)]
path = deque()

for i in range(1, len(data1)+1):
    for j in range(1, len(data2)+1):
        if data1[i-1] == data2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(data1)][len(data2)])

# LCS 구현 함수
def getText(r,c):
    if r == 0 or c == 0:    # 둘 중에 끝나면
        return
    if data1[r-1] == data2[c-1]:
        path.append(data1[r-1])
        getText(r-1,c-1) # 대각선 위로 감
    else:   # 다르면 왼쪽, 위 둘 중 큰 값으로 감
        if dp[r-1][c] > dp[r][c-1]: # 다를 때 위쪽 값이 큰 경우
            getText(r-1,c)
        else:   # 다를 때 왼쪽 값이 큰 경우
            getText(r, c-1)

getText(len(data1), len(data2))

while len(path) > 0:
    print(path.pop(), end='')