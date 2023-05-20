import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,1,-1]

graph = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
def bfs(a,b):
    queue = deque([(a,b)])
    visited[a][b] = True
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                elif graph[nx][ny] == 0:
                    continue
            
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and not visited[i][j]:
            graph[i][j] = 0
            bfs(i,j)
            
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1
            
for k in range(n):
    print(' '.join(map(str, graph[k])))
    
    
    