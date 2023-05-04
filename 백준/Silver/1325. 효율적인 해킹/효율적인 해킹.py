import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start):
    count = 1
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
result = []
max_count = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

for i in range(1, n+1):
    count = bfs(graph, i)
    if count > max_count:
        max_count = count
    result.append([i, count])

for res in result:
    if res[1] == max_count:
        print(res[0], end= ' ')



            