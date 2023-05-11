import sys

input = sys.stdin.readline
INF = 1e9
n = int(input())
W = []

for _ in range(n):
    W.append(list(map(int,input().split())))

dp = [[0 for j in range(1 << 16)] for i in range(16)]

def tsp(c, v):  # 현재 위치 'c' 방문한 도시들의 비트 마스크 'v'
    if v == (1 << n) - 1:   # 모든 노드를 방문한 경우
        if W[c][0] == 0:   
            return INF
        else:
            return W[c][0]
    
    if dp[c][v] != 0: # 이미 방문한 노드인 경우
        return dp[c][v]
    
    result = INF
    for i in range(0, n):
        # 방문한 적이 없고, 갈 수 있는 도시인 경우
        if (v & (1 << i)) == 0 and W[c][i] != 0:
            result = min(result, tsp(i, (v | (1 << i))) + W[c][i])
    
    dp[c][v] = result
    return dp[c][v]

print(tsp(0, 1))
