import sys

sys.setrecursionlimit(10**6)

n = int(input())
graph = []
result = 1e9
visited = [False] * n
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(graph, start, now, cost):
    global result
    if start == now and visited.count(False) == 0:
        result = min(result, cost)

    for i in range(n):
        if graph[now][i] != 0 and not visited[i]:
            visited[i] = True
            dfs(graph, start, i, cost + graph[now][i])
            visited[i] = False

dfs(graph, 0, 0, 0)
print(result)
