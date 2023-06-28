import sys
from collections import deque


input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = []

max_num = 0

for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for i in data:
        if i > max_num:
            max_num = i

def bfs(x, y, num):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > num:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

result = []

for i in range(max_num):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and not visited[j][k]:
                bfs(j, k, i)
                cnt += 1
    result.append(cnt)

print(max(result))
