import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
n = int(input())
visited = [[False] * n for _ in range(n)]

# 적록색약이 아닐 때 결과값, 적록색약일 때 결과값
result1 = 0
result2 = 0

for _ in range(n):
    graph.append(list(input()))

def dfs(graph, x, y):
    now = graph[x][y]
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == now:
                dfs(graph,nx,ny)

for a in range(n):
    for b in range(n):
        if visited[a][b] == False:
            dfs(graph, a, b)
            result1 += 1

# R - G 똑같이 만듬
for c in range(n):
    for d in range(n):
        if graph[c][d] == "G":
            graph[c][d] = "R"

visited = [[False] * n for _ in range(n)]

for e in range(n):
    for f in range(n):
        if visited[e][f] == False:
            dfs(graph, e, f)
            result2 += 1

print(result1, result2)



 

