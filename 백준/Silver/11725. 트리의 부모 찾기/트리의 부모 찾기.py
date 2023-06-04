import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [i for i in range(n+1)]

for _ in range(n-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
    
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(graph, i, visited)
            
dfs(graph,1,visited)

for j in range(2, n+1):
    print(parent[j])
            
            