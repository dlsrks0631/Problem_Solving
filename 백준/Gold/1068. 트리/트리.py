import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input()) # 노드 개수
parent = list(map(int,input().split()))
delete_node = int(input()) # 삭제할 노드

result = 0
root = 0
visited = [False] * (n+1)
graph = [[] for _ in range(n)]

for i in range(n):
    if parent[i] != -1:
        graph[i].append(parent[i])
        graph[parent[i]].append(i)
    else:
        root = i
        
def dfs(graph, v, visited):
    global result
    child = 0
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i] and i != delete_node:
            child += 1
            dfs(graph, i, visited)
    
    if child == 0:
        result += 1

if delete_node == root:
    print(0)
else:
    dfs(graph, root, visited)
    print(result)
        

