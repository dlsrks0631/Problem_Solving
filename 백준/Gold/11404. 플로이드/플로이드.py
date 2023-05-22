import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = sys.maxsize

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0
    
for _ in range(m):
    s,e,cost = map(int,input().split())
    if graph[s][e] > cost:
        graph[s][e] = cost
    
for a in range(1, n+1): # 사이값 - k
    for b in range(1, n+1):
        for c in range(1, n+1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])
            
for j in range(1, n+1):
    for k in range(1, n+1):
        if graph[j][k] == INF:
            print(0, end=' ')
        else:
            print(graph[j][k], end=' ')
    print()
    